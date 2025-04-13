from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self, value, tag, props=None):
        super().__init__(tag, value, props)