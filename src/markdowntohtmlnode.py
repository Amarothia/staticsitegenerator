from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from blockconversions import markdown_to_blocks, block_to_block_type, BlockType, blocks_to_parent_nodes
from inlineconversions import text_to_textnodes
from textnodetohtmlnode import text_node_to_html_node

def markdown_to_html_node(text):
    blocks_list = markdown_to_blocks(text) # this simply creates filtered list of strings
    parent_nodes = blocks_to_parent_nodes(blocks_list) 
    return ParentNode("div", parent_nodes)
