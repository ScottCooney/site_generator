import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    # Your test methods go here
    
    def test_props_to_html_no_props(self):
        # Test with no props
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())
        
    def test_props_to_html_one_prop(self):
        # Test with one prop
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(' href="https://www.google.com"', node.props_to_html())
        
    def test_props_to_html_multiple_props(self):
        # Test with multiple props
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', result)
        self.assertIn(' target="_blank"', result)

if __name__ == "__main__":
    unittest.main()