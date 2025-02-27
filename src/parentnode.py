from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list = None, props: dict = None):
        if tag == None or not isinstance(tag, str):
            raise ValueError("Parentnode must have a tag value of str.")
        if children == None or not isinstance(children, list):
            raise ValueError("Parentnode must have a child node. It cares so you don't have to.")
        super().__init__(tag, None, children, props)

    def to_html(self):
        html_output = ""
        if self.props != None:
                html_output += f"<{self.tag}{self.props_to_html()}>"
        html_output += f"<{self.tag}>"
        for child in self.children:
            if self.props != None:
                html_output += f"{child.to_html()}"
            html_output += f"{child.to_html()}"
        html_output += f"</{self.tag}>"
        return html_output
        