import unittest

from textnode import TextNode, TextType
from textnodetohtmlnode import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        # print("\n" + html_node.to_html())
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        # print("\n" + html_node.to_html())
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_link_with_url(self):
        node = TextNode("Google", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        # print("\n" + html_node.to_html())
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_link_with_image(self):
        node = TextNode("Google Cookies!", TextType.IMAGE, "https://www.google.com/googleCookies.png")
        html_node = text_node_to_html_node(node)
        # print("\n" + html_node.to_html())
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.google.com/googleCookies.png", "alt": "Google Cookies!"})


if __name__ == "__main__":
    unittest.main()