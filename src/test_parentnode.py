import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_rigorous(self):
        p2_node = LeafNode("p", "Paragraph 2")
        p1_node = LeafNode("p", "Paragragh 1")
        h1_node = LeafNode("h1", "Front-end Development is the Worst")
        body_node = ParentNode('body', [h1_node, p1_node, p2_node])
        title_node = LeafNode('title', "Why Frontend Development Sucks")
        head_node = ParentNode('head', [title_node])
        rootnode = ParentNode('html', [head_node, body_node])
        print(rootnode.to_html())


if __name__ == "__main__":
    unittest.main()