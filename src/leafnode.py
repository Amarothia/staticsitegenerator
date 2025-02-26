from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None):
        if isinstance(tag, HTMLNode) or isinstance(value, HTMLNode) or isinstance(props, HTMLNode):
            raise ValueError("LeafNode objects cannot have children")
        if value == None:
            raise ValueError("LeafNode.value cannot be None")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == None:
            return self.value
        if self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"