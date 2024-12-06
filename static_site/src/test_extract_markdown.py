import unittest
from inline_markdown import *

class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_mixed_content(self):
        text = "Here's an image ![alt text](https://example.com/image.png) and a [link](https://example.com)."
        images = [("alt text", "https://example.com/image.png")]
        links = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_images(text), images)
        self.assertEqual(extract_markdown_links(text), links)

    def test_no_images(self):
        text = "This is a link [to Google](https://google.com) with no images."
        self.assertEqual(extract_markdown_images(text), [])

    def test_no_links(self):
        text = "This is an image ![sunset](https://example.com/sunset.jpg) with no links."
        self.assertEqual(extract_markdown_links(text), [])

    def test_empty_text(self):
        text = ""
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

    def test_multiple_images(self):
        text = "![Image1](https://example.com/1.png)![Image2](https://example.com/2.png)"
        expected = [
            ("Image1", "https://example.com/1.png"),
            ("Image2", "https://example.com/2.png")
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_multiple_links(self):
        text = "[Link1](https://example.com/1)[Link2](https://example.com/2)"
        expected = [
            ("Link1", "https://example.com/1"),
            ("Link2", "https://example.com/2")
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )
    def test_text_to_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertEqual([
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
], text_to_textnodes(text))
        
    def test_no_text(self):
        text = ''
        self.assertFalse(text_to_textnodes(text))

    def test_extract_title(self):
        # Test a simple case
        assert extract_title("# Hello World") == "Hello World"

    def test_no_header(self):
        markdown = "Hello World"
        try:
            extract_title(markdown)
            assert False, "Should have raised exception"
        except Exception as e:
            assert str(e) == "No header!"


    def test_header_strip(self):
        assert(extract_title('#          Hello World') == 'Hello World')
    
        

if __name__ == "__main__":
    unittest.main()
