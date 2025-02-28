import unittest

from textnode import TextType, TextNode


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


if __name__ == "__main__":
    unittest.main()