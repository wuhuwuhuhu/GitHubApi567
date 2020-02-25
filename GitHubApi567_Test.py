"""This is test file for GitHubApi567
    Written by Haodong Wu
"""
from GitHubApi567 import repository_get, commit_get
import unittest
from unittest.mock import Mock,patch
import json
class TestGitHubApi567(unittest.TestCase):
    
    @patch('requests.get')
    def test_repository_get(self, mockedReq):
        #side_effects = ['[{"name": "hellogitworld"}]'.encode]
        #mockedReq.side_effect = ['[{"name": "hellogitworld"}]','[{"commit":{}},{"commit":{}}]']
        mockedReq.return_value.text = '[{"name": "hellogitworld"}]'
        self.assertEqual(repository_get('richkempinski'), [('hellogitworld', 1)])

    @patch('requests.get')
    def test_commit_get(self,mockedReq):
        mockedReq.return_value.text = '[{"commit":{}},{"commit":{}}]'
        self.assertAlmostEqual(commit_get('richkempinski','hellogitworld'),2)

if __name__ == "__main__":
    unittest.main(exit = False, verbosity= 2)