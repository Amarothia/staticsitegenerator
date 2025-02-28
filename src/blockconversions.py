from enum import Enum
from textnode import TextNode, TextType
from textnodetohtmlnode import text_node_to_html_node
from inlineconversions import text_to_textnodes
from parentnode import ParentNode
from leafnode import LeafNode


class BlockType(Enum):
    HEADING = "heading" # a heading: begins with 1-6 #'s
    CODE = "code" # a block of code: begins and ends with ```
    QUOTE = "quote" # a quote block: each line begins with >
    UNORDERED_LIST = "unordered list" # an unordered list: each line begins with -
    ORDERED_LIST = "ordered list" # an ordered list: begins with 1. and iterates from there on each line
    PARAGRAPH = "paragraph" # a regular paragraph

def block_to_block_type(text: str):
    # Check for heading
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    # Check for code block
    elif text.startswith("```") and text.endswith("```"):
        return BlockType.CODE
    
    # Split into lines for other checks
    lines = text.split("\n")
    
    # Check for quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list
    if (len(lines) > 0 and lines[0].startswith("1. ") and all(line.startswith(f"{i+1}. ") for i, line in enumerate(lines))):
        return BlockType.ORDERED_LIST
    
    # Default to paragraph
    return BlockType.PARAGRAPH


def markdown_to_blocks(text: str) -> list[str]:
    # Split into blocks and filter out empty ones
    list_of_blocks = [block.strip() for block in text.split('\n\n') if block.strip()]
    
    # Process each block to handle indentation with a list comprehension, alternate option for my notes.
    return ['\n'.join([line.strip() for line in block.split('\n')]) for block in list_of_blocks]

def blocks_to_parent_nodes(blocks: list[str]):
    parent_nodes = []
    for text in blocks:
        # This does inline conversions of all the blocks and adds them to the html_list
        match block_to_block_type(text):

            case BlockType.HEADING:
                index = text.find(" ") # tells us where the #'s stop and the actual text begins, and also the number of #'s
                heading_text = text[index+1:]
                parent_nodes.append(ParentNode(f"h{index}", [text_node_to_html_node(node) for node in text_to_textnodes(heading_text)]))

            case BlockType.QUOTE:
                cleaned_quote_text = '\n'.join([line.replace(">", "") for line in text.split("\n") if line.startswith(">")])
                parent_nodes.append(ParentNode("blockquote", [text_node_to_html_node(node) for node in text_to_textnodes(cleaned_quote_text)]))

            case BlockType.UNORDERED_LIST:
                parent_nodes.append(ParentNode("ul", [
                    ParentNode("li", [text_node_to_html_node(node) for node in text_to_textnodes(line[2:])]) for line in text.split('\n')]))
                
            case BlockType.ORDERED_LIST:
                parent_nodes.append(ParentNode("ol", [
                    ParentNode("li", [text_node_to_html_node(node) for node in text_to_textnodes(line[3:])]) for line in text.split('\n')]))

            case BlockType.PARAGRAPH:
                parent_nodes.append(ParentNode("p", [text_node_to_html_node(node) for node in text_to_textnodes(text.replace('\n', " "))]))

            case BlockType.CODE:
                parent_nodes.append(ParentNode("pre", [ParentNode("code", [LeafNode(None, text[3:-3])])]))
    
    return parent_nodes
