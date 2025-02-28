import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    # This function only handles bold, italics and code. Image and Link will be handled later or in a different function.
    new_nodes = []

    for node in old_nodes: # node is a TextNode
        sub_nodes = []
        counter = 2
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if delimiter in node.text:
                sub_nodes = node.text.split(delimiter) # breaking node's text value into a sub list
                if len(sub_nodes) % 2 == 0:
                    raise ValueError(f"Unmatched delimiters found in text: {node.text}")
                for sub_node_string in sub_nodes: # using that string
                    if counter % 2 == 0: # this accomodates any number of special words in the text
                        if sub_node_string != "":
                            new_nodes.append(TextNode(sub_node_string, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(sub_node_string, text_type))
                    counter += 1
            else:
                new_nodes.append(node)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes: # node is a TextNode
        sub_nodes = []
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            extracted_tuples = extract_markdown_images(node.text)
            if len(extracted_tuples) != 0:
                for tuple in extracted_tuples:
                    if len(sub_nodes) == 0: # for the first split
                        sub_nodes = node.text.split(f'![{tuple[0]}]({tuple[1]})', 1)
                        if sub_nodes[1] != "": # for other splits if more than one image
                            substring = sub_nodes[1]
                    else:
                        sub_nodes = substring.split(f'![{tuple[0]}]({tuple[1]})', 1)
                    if sub_nodes[0] != "":
                        new_nodes.append(TextNode(sub_nodes[0], TextType.TEXT))
                    new_nodes.append(TextNode(f"{tuple[0]}", TextType.IMAGE, f"{tuple[1]}"))
                if sub_nodes[1] != "":
                    new_nodes.append(TextNode(sub_nodes[1], TextType.TEXT))
            else:
                new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes: # node is a TextNode
        sub_nodes = []
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            extracted_tuples = extract_markdown_links(node.text)
            if len(extracted_tuples) != 0:
                for tuple in extracted_tuples:
                    if len(sub_nodes) == 0: # for the first split
                        sub_nodes = node.text.split(f'[{tuple[0]}]({tuple[1]})', 1)
                        if sub_nodes[1] != "": # for other splits if more than one link
                            substring = sub_nodes[1]
                    else:
                        sub_nodes = substring.split(f'[{tuple[0]}]({tuple[1]})', 1)
                    if sub_nodes[0] != "":
                        new_nodes.append(TextNode(sub_nodes[0], TextType.TEXT))
                    new_nodes.append(TextNode(f"{tuple[0]}", TextType.LINK, f"{tuple[1]}"))
                if sub_nodes[1] != "":
                    new_nodes.append(TextNode(sub_nodes[1], TextType.TEXT))
            else:
                new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    nodes = []
    if text != "":
        nodes = [TextNode(text)]
        nodes = split_nodes_image(nodes)
        nodes = split_nodes_link(nodes)
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
