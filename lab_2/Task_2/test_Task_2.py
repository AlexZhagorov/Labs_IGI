import unittest
import re

from commands import reg

class MyTest(unittest.TestCase):
    def test_CommandRegEx(self):
        match_obj = re.match(reg, "add \"Mister\"")
        self.assertEqual(match_obj.group(1), "add")
        self.assertEqual(match_obj.group(2), " \"Mister\"")
        self.assertEqual(match_obj.group(3), "Mister")
        
        match_obj = re.match(reg, "save")
        self.assertEqual(match_obj.group(1), "save")
        self.assertEqual(match_obj.group(2), None)