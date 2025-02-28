from enum import Enum
from textnode import TextNode, TextType


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


def markdown_to_blocks(text: str):
    # Split into blocks and filter out empty ones
    list_of_blocks = [block.strip() for block in text.split('\n\n') if block.strip()]
    
    # Process each block to handle indentation with a list comprehension, alternate option for my notes.
    return ['\n'.join([line.strip() for line in block.split('\n')]) for block in list_of_blocks]
