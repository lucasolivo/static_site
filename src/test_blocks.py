import unittest
from markdown_blocks import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
)

class TestMarkdownToBlocks(unittest.TestCase):

    def test_basic_split(self):
        markdown = "# Heading\n\nParagraph text here.\n\n* List item"
        expected_blocks = [
            "# Heading",
            "Paragraph text here.",
            "* List item"
        ]
        result = markdown_to_blocks(markdown)  # Assume you have this function implemented
        self.assertEqual(result, expected_blocks)

    def test_leading_trailing_whitespace(self):
        markdown = "\n\n  # Heading  \n\n  Paragraph text  \n\n  "
        expected_blocks = [
            "# Heading",
            "Paragraph text"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected_blocks)

    def test_excessive_newlines(self):
        markdown = "# Heading\n\n\n\nParagraph text"
        expected_blocks = [
            "# Heading",
            "Paragraph text"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected_blocks)

    def test_header(self):
        text = "###### yeet"
        self.assertEqual("heading", block_to_block_type(text))

    def test_code(self):
        text = '```yeet```'
        self.assertEqual("code", block_to_block_type(text))
    
    def test_quote(self):
        text = '>flipping pancakes'
        self.assertEqual('quote', block_to_block_type(text))

    def test_list_asterisk(self):
        text = '* yeet\n\n* yeet'
        self.assertEqual('unordered_list', block_to_block_type(text))

    def test_list_line(self):
        text = '- yeet\n\n- yeet'
        self.assertEqual('unordered_list', block_to_block_type(text))

    def test_list_ordered(self):
        text = '1. yeet\n\n2. yeet'
        self.assertEqual('ordered_list', block_to_block_type(text))

    def test_paragraph(self):
        text = '*yeet1foot'
        self.assertEqual('paragraph', block_to_block_type(text))

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is a code block
```

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is a code block\n</code></pre><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()