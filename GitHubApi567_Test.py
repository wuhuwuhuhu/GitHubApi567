"""This is test file for GitHubApi567
    Written by Haodong Wu
"""
from GitHubApi567 import repository_get
import unittest

class GitHubApi567(unittest.TestCase):
    def test_repository_get(self):
        self.assertEqual(repository_get('richkempinski'), [('hellogitworld', 30), ('helloworld', 6), ('Mocks', 10), ('Project1', 2), ('threads-of-life', 1)])

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)