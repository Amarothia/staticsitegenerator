import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_empty_props(self):
        node = LeafNode("p", "Hello, world!", {})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_raises_value_error_for_children(self):
        with self.assertRaises(ValueError):
            LeafNode("p", "Hello, world!", LeafNode("a", "link"))


if __name__ == "__main__":
    unittest.main()