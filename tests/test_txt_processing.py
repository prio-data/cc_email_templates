
import unittest
from cc_email_templates import txt_processing

class TestTxtProc(unittest.TestCase):
    def test_deduplicate(self):
        t = ["a","b","b","b","c"]
        self.assertEqual(txt_processing.deduplicate(t), ["a","b","c"])
