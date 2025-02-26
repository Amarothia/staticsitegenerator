class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # p, a, h1, etc
        self.value = value # the text inside of the paragraph
        self.children = children # a list of HTMLNode objects that are children of this one
        self.props = props # a dict representing the attributes fo the tag, for example a link <a> might have {"href":"https://www.google.com"}

        # An HTMLNode without a tag will just render as raw text
        # An HTMLNode without a value will be assumed to have children
        # An HTMLNode without children will be assumed to have a value
        # An HTMLNode without props simply won't have any attributes

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        HTML_attributes = ""
        for key in self.props:
            HTML_attributes += f" {key}={self.props[key]}"
        return HTML_attributes
    
    def __repr__(self):
        if self.props != None:
            return f"[Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props_to_html()}]"
        return f"[Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: None]"