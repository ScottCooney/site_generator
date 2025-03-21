class HTMLNode:
    def __init__(self,tag= None,value= None,children=None,props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props == None:
            return ""
        temp_str= ""
        for key in self.props.keys():
            temp_str = temp_str + " " + key + "=\"" + self.props[key] + "\""
        return temp_str