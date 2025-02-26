import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    embedded_link_node = HTMLNode("a", "backend", None, {"href":"https://www.boot.dev"})
    p2_node = HTMLNode("p", "Paragraph 2", embedded_link_node, None)
    p1_node = HTMLNode("p", "Paragragh 1", None, None)
    h1_node = HTMLNode("h1", "Front-end Development is the Worst", None, None)
    body_node = HTMLNode('body', None, [h1_node, p1_node, p2_node], None)
    link_node = HTMLNode('link', None, None, {"rel":"stylesheet", "href":"/styles.css"})
    title_node = HTMLNode('title', "Why Frontend Development Sucks", None, None)
    head_node = HTMLNode('head', None, [title_node, link_node], None)
    rootnode = HTMLNode('html', None, [head_node, body_node], None)
    node_list = [embedded_link_node, p2_node, p1_node, h1_node, body_node, link_node, title_node, head_node, rootnode]

    def test_HTMLNode_not_eq(self):
        self.assertNotEqual(self.p1_node, self.p2_node)

    def test_HTMLNode_print_all_nodes(self):
        nodelist = self.node_list
        print()
        print(*nodelist, sep='\n')

if __name__ == "__main__":
    unittest.main()