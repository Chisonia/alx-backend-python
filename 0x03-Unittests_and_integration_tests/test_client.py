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

    @patch("client.GithubOrgClient.org")
    def test_public_repos_url(self, mock_org):

        '''Test that the _public_repos_url method returns
        the correct URL based on the org payload
        and that the result is memoized after the first call.

        Args:
            mock_org (Mock): The mock object for the
            GithubOrgClient.org method.'''

        # Define a mocked payload for the org
        mock_org.return_value = {
            "login": "google",
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        # Create an instance of GithubOrgClient with the mock org
        client = GithubOrgClient("google")

        # First call to _public_repos_url
        result = client._public_repos_url

        # Assert the repos_url is correctly fetched from the mocked payload
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")  # noqa: E501

        # Verify that the org method was called once
        mock_org.assert_called_once()

        # Call _public_repos_url again to test memoization
        result_again = client._public_repos_url

        # Assert the second call returns the same result
        self.assertEqual(result_again, result)

        # Ensure org was still only called once
        mock_org.assert_called_once()


if __name__ == "__main__":
    unittest.main()
