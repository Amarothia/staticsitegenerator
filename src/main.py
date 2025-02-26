from textnode import TextType, TextNode

def main():
    text = "this is a test"
    text_type = TextType.BOLD_TEXT
    url = "https://www.boot.dev"
    new_text_node = TextNode(text, text_type, url)
    print(new_text_node)

main()