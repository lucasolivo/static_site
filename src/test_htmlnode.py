import unittest

from htmlnode import HTMLNODE

class test_HTMLNODE(unittest.TestCase):
    def test_error(self):
        node = HTMLNODE()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_no_prop(self):
        node = HTMLNODE()
        self.assertEqual("", node.props_to_html())

    def test_single_prop(self):
        prop = {"href": "https://www.google.com"}
        node = HTMLNODE(props=prop)
        self.assertEqual('href="https://www.google.com"', node.props_to_html())

    def test_multi_prop(self):
        prop = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNODE(props=prop)
        self.assertEqual('href="https://www.google.com" target="_blank"', node.props_to_html())

if __name__ == "__main__":
    unittest.main()