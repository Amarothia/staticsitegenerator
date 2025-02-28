import unittest

from textnode import TextType, TextNode
from inlineconversions import split_nodes_delimiter, split_nodes_image, split_nodes_link, extract_markdown_links, extract_markdown_images, text_to_textnodes


class TestInlineConversions(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is my **boom** stick!", TextType.TEXT)
        node1 = TextNode("This is my ", TextType.TEXT)
        node2 = TextNode("boom", TextType.BOLD)
        node3 = TextNode(" stick!", TextType.TEXT)
        html_node_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(html_node_list, [node1, node2, node3])

    def test_split_nodes_delimiter_italics_first_word(self):
        node = TextNode("_The Necronomicon_, a book for all ages!", TextType.TEXT)
        node1 = TextNode("The Necronomicon", TextType.ITALIC)
        node2 = TextNode(", a book for all ages!", TextType.TEXT)
        html_node_list = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(html_node_list, [node1, node2])

    def test_split_nodes_delimiter_code_last_word(self):
        node = TextNode("I'm the man with the plan, here's my code `typety typety type type`", TextType.TEXT)
        node1 = TextNode("I'm the man with the plan, here's my code ", TextType.TEXT)
        node2 = TextNode("typety typety type type", TextType.CODE)
        html_node_list = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(html_node_list, [node1, node2])

    def test_split_nodes_delimiter_multiple_words(self):
        node = TextNode("This is my **boom** stick, beware my **wrath**!", TextType.TEXT)
        node1 = TextNode("This is my ", TextType.TEXT)
        node2 = TextNode("boom", TextType.BOLD)
        node3 = TextNode(" stick, beware my ", TextType.TEXT)
        node4 = TextNode("wrath", TextType.BOLD)
        node5 = TextNode("!", TextType.TEXT)
        html_node_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(html_node_list, [node1, node2, node3, node4, node5])

    def test_split_nodes_delimiter_not_TEXT_type(self):
        node = TextNode("This is my **boom** stick!", TextType.BOLD)
        html_node_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(html_node_list, [node])

    def test_split_nodes_delimiter_unmatched_delimiters(self):
        node = TextNode("This is my **boom stick!", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertTrue("unmatched" in str(context.exception).lower())

    def test_split_nodes_delimiter_empty_node_list(self):
        html_node_list = split_nodes_delimiter([], "**", TextType.BOLD)
        self.assertEqual(html_node_list, [])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images("This is text with an ![alt text one](https://i.imgur.com/zjjcJKZ.png) and another ![alt text two](https://i.imgur.com/3elNhQu.png)")
        self.assertListEqual([("alt text one", "https://i.imgur.com/zjjcJKZ.png"), ("alt text two", "https://i.imgur.com/3elNhQu.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with an [anchor text](https://i.imgur.com/zjjcJKZ)")
        self.assertListEqual([("anchor text", "https://i.imgur.com/zjjcJKZ")], matches)
    
    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links("This is text with an [anchor text one](https://i.imgur.com/zjjcJKZ) and another [anchor text two](https://i.imgur.com/3elNhQu)")
        self.assertListEqual([("anchor text one", "https://i.imgur.com/zjjcJKZ"), ("anchor text two", "https://i.imgur.com/3elNhQu")], matches)


    def test_split_images_multiple(self):
        node = TextNode(
            "This is text with an ![alt text one](https://i.imgur.com/zjjcJKZ.png) and another ![alt text two](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("alt text one", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("alt text two", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_link_multiple(self):
        node = TextNode(
            "This is text with a link: [anchor text one](https://i.imgur.com/zjjcJKZ) and another link: [anchor text two](https://i.imgur.com/3elNhQu)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link: ", TextType.TEXT),
                TextNode("anchor text one", TextType.LINK, "https://i.imgur.com/zjjcJKZ"),
                TextNode(" and another link: ", TextType.TEXT),
                TextNode("anchor text two", TextType.LINK, "https://i.imgur.com/3elNhQu"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ], nodes
        )
    def test_text_to_textnodes_empty_string(self):
        text = ""
        nodes = text_to_textnodes(text)
        self.assertListEqual([], nodes)

if __name__ == "__main__":
    unittest.main()