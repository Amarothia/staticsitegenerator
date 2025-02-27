from textnode import TextType, TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnodetohtmlnode import text_node_to_html_node


def main():
    text = "this is a test"
    text_type = TextType.BOLD
    url = "https://www.boot.dev"
    new_text_node = TextNode(text, text_type, url)
    print(new_text_node)

if __name__ == "__main__":
    main()