import unittest

from textnode import TextType, TextNode
from blockconversions import BlockType, markdown_to_blocks, block_to_block_type

class TestBlockConversions(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_type(self):
        heading_block = "# heading block"
        code_block = "```This is a code block\nIt has various pieces of code in it\nAll for the good of mankind of course.```"
        quote_block = ">This is a quote block\n>Wherein many things are quoted\n>So let's make sure it's working!"
        unordered_list_block = "- Thing One\n- Thing Two\n- Thing Red\n- Thing Blue"
        ordered_list_block = "1. Gather our forces.\n2. Make our plans.\n3. Rule the world."
        regular_block = "This is just a boring\nold block of text."
        block_list = [heading_block, code_block, quote_block, unordered_list_block, ordered_list_block, regular_block]
        block_type_list = []
        for block in block_list:
            block_type_list.append(block_to_block_type(block).value)
        self.assertEqual(["heading", "code", "quote", "unordered list", "ordered list", "paragraph"], block_type_list)

    def test_block_to_block_type_misleading_data(self):
        heading_block = "####### heading block"
        code_block = "```This is a code block\nIt has various pieces of code in it\nAll for the good of mankind of course."
        quote_block = ">This is a quote block\nWherein many things are quoted\n>So let's make sure it's working!"
        unordered_list_block = "- Thing One\n- Thing Two\n3. Thing Red\n- Thing Blue"
        ordered_list_block = "1. Gather our forces.\n2. Make our plans.\n!!!. Rule the world."
        regular_block = "This is just a boring\nold block of text.\n\n\n"
        block_list = [heading_block, code_block, quote_block, unordered_list_block, ordered_list_block, regular_block]
        block_type_list = []
        for block in block_list:
            block_type_list.append(block_to_block_type(block).value)
        self.assertEqual(["paragraph", "paragraph", "paragraph", "paragraph", "paragraph", "paragraph", ], block_type_list)


if __name__ == "__main__":
    unittest.main()