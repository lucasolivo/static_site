class HTMLNODE:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        prop_string = ""
        if not self.props:
            return prop_string
        for i in self.props:
            if prop_string:
                prop_string = prop_string + ' '
            prop_string = f'{prop_string}{i}="{self.props[i]}"'
        return prop_string
    
    def __repr__(self):
        print(f"tag: {self.tag} props: {self.props} children: {self.children} value: {self.value}")
    
    
class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        children = None
        super().__init__(tag=tag, value=value, children=children, props=props)
    
    def to_html(self):
        print(f'value: {self.value}')
        if self.tag == "img":
        # Ensure `props` contains `src` and `alt`
            src = self.props.get("src", "")
            alt = self.props.get("alt", "")
            return f'<img src="{src}" alt="{alt}">'
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        else:
            tag = ""
            if self.props:
                tag = f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
                return tag
            else:
                tag = f'<{self.tag}>{self.value}</{self.tag}>'
                return tag
            
    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return (self.tag == other.tag and
                    self.value == other.value and
                    self.props == other.props)
        return False
            
class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No Tag")
        if not self.children:
            raise ValueError("Childless cat lady")
        else:
            str = f'<{self.tag}>'
            for child in self.children:
                str = str + child.to_html()
            str = str + f"</{self.tag}>"
            return str