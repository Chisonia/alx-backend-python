#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Tests for the GithubOrgClient.org method.'''

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):

        '''Test that GithubOrgClient.org returns
        the correct value.

        Args:
            org_name (str): The organization name to test.
            mock_get_json (Mock): The mock object for
            the get_json function.'''

        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org

        # Check that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")  # noqa: E501

        # Verify the result matches the expected return value
        self.assertEqual(result, {"login": org_name})


if __name__ == "__main__":
    unittest.main()
