import unittest

from htmlnode import HTMLNODE, LeafNode

class test_LeafNode(unittest.TestCase):
    def test_no_val(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = LeafNode(None, "I do not like asparagus")
        self.assertEqual("I do not like asparagus", node.to_html())

    def test_tag_with_tag(self):
        node = LeafNode('p', "I do not like asparagus")
        self.assertEqual("<p>I do not like asparagus</p>", node.to_html())

    def test_with_props(self):
        node = LeafNode('a', "I do not like asparagus", {"href": "https://www.google.com"})
        self.assertEqual('<a href="https://www.google.com">I do not like asparagus</a>', node.to_html())

if __name__ == "__main__":
    unittest.main()