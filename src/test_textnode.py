import unittest

from textnode import TextNode, TextType, split_nodes_delimiter


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.BOLD, "url")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "url")
        node2 = TextNode("This is a text node", TextType.ITALIC, "url")
        self.assertNotEqual(node, node2)

    def test_no_url_eq(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)

    def test_no_url_noteq(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr_eq(self):
        node = TextNode("This is a text node", TextType.LINK, "url")
        node2 = TextNode("This is a text node", TextType.LINK, "url")
        self.assertEqual(str(node), str(node2))

    def test_repr_noteq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "url")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(str(node), str(node2))

    # Set of tests for deliminter splitting of old TextNodes

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

if __name__ == "__main__":
    unittest.main()