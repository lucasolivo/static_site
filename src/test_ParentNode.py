import unittest

from htmlnode import HTMLNODE, LeafNode, ParentNode

class test_ParentNode(unittest.TestCase):
    def test_no_tag_error(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node.tag = None
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node.children = None
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
            node.to_html()
        )

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ]
                ),
                LeafNode("i", "Italic text"),
            ],
        )
        self.assertEqual(
            '<div><p><b>Bold text</b>Normal text</p><i>Italic text</i></div>',
            node.to_html()
        )

    def test_multiple_children(self):
        node = ParentNode(
            "ul",
            [
                ParentNode(
                    "li",
                    [LeafNode(None, "First item")]
                ),
                ParentNode(
                    "li",
                    [LeafNode(None, "Second item")]
                ),
            ],
        )
        self.assertEqual(
            '<ul><li>First item</li><li>Second item</li></ul>',
            node.to_html()
        )

    def test_empty_children_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_leaf_nodes_with_none_tags(self):
        node = ParentNode(
            "div",
            [
                LeafNode(None, "Some text"),
                LeafNode(None, "More text"),
            ]
        )
        self.assertEqual('<div>Some textMore text</div>', node.to_html())

    def test_parent_node_with_only_parent_children(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "Paragraph 1"),
                    ]
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "Paragraph 2"),
                    ]
                ),
            ],
        )
        self.assertEqual(
            '<div><p>Paragraph 1</p><p>Paragraph 2</p></div>',
            node.to_html()
        )

    def test_large_nested_structure(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "header",
                            [LeafNode(None, "Title")]
                        ),
                        ParentNode(
                            "article",
                            [
                                LeafNode(None, "Content starts here."),
                                ParentNode(
                                    "footer",
                                    [LeafNode(None, "Footer text")]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        self.assertEqual(
            '<div><section><header>Title</header><article>Content starts here.<footer>Footer text</footer></article></section></div>',
            node.to_html()
        )

    def test_recursive_to_html_call(self):
        child = ParentNode(
            "span",
            [
                LeafNode(None, "Nested text")
            ]
        )
        node = ParentNode(
            "div",
            [child]
        )
        self.assertEqual('<div><span>Nested text</span></div>', node.to_html())


if __name__ == "__main__":
    unittest.main()