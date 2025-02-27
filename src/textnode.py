from enum import Enum
import re

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text: str, text_type: TextType = TextType.TEXT, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

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
    return re.findall(r"!\[(.*)\]\((.*)\)(?:\s|$)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*)\]\((.*)\)(?:\s|$)", text)


