import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_function(self):
        node = TextNode("This is a text node", TextType.BOLD, 'http://www.google.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'http://www.google.com')
        self.assertEqual(True, node.__eq__(node2))

    def test_nourl(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_different_text(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text_type, TextType.ITALIC)

    def test_text_to_html(self):
        node = TextNode('yeet', TextType.TEXT)
        self.assertTrue(LeafNode(None, 'yeet').__eq__(text_node_to_html_node(node)))

    def test_bold_to_html(self):
        node = TextNode('yeet', TextType.BOLD)
        self.assertTrue(LeafNode('b', 'yeet').__eq__(text_node_to_html_node(node)))
    
    def test_italic_to_html(self):
        node = TextNode('yeet', TextType.ITALIC)
        self.assertTrue(LeafNode('i', 'yeet').__eq__(text_node_to_html_node(node)))

    def test_code_to_html(self):
        node = TextNode('yeet', TextType.CODE)
        self.assertTrue(LeafNode('code', 'yeet').__eq__(text_node_to_html_node(node)))

    def test_link_to_html(self):
        node = TextNode('yeet', TextType.LINK, 'https://www.google.com')
        self.assertTrue(LeafNode('a', 'yeet', {'href': 'https://www.google.com'}).__eq__(text_node_to_html_node(node)))

    def test_image_to_html(self):
        node = TextNode('yeet', TextType.IMAGE, 'https://www.google.com')
        self.assertTrue(LeafNode('img', '', {'src': 'https://www.google.com', 'alt': 'yeet'}).__eq__(text_node_to_html_node(node)))

if __name__ == "__main__":
    unittest.main()