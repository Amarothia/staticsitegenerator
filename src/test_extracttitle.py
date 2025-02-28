import unittest

from extracttitle import extract_title


class TestExtracttitle(unittest.TestCase):

    def test_extract_title(self):
        md_text = "# The Easy One"
        md_text_inside_stuff = "Not as easy \n# But still not too hard!"
        md_text_some_extra_tricks = "And what \n## if there's other \n# Stuff involved\n in the situation?"
        md_list = [md_text, md_text_inside_stuff, md_text_some_extra_tricks]
        title_list = [extract_title(text) for text in md_list]
        self.assertListEqual(title_list, ["The Easy One", "But still not too hard!", "Stuff involved"])


if __name__ == "__main__":
    unittest.main()