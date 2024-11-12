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

    @patch("client.GithubOrgClient.get_json")
    @patch("client.GithubOrgClient._public_repos_url")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):

        '''Test that the public_repos method returns the
        correct repositories list when the _public_repos_url
        and get_json methods are mocked.

        Args:
            mock_public_repos_url (Mock): The mock for the
            _public_repos_url method. mock_get_json (Mock):
            The mock for the get_json method.'''

        # Mock the return value of _public_repos_url
        mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"  # noqa: E501

        # Mock the return value of get_json (the repository payload)
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Create an instance of GithubOrgClient with the mock URL
        client = GithubOrgClient("google")

        # Call the public_repos method
        repos = client.public_repos()

        # Assert the list of repos matches the mocked payload
        self.assertEqual(repos, ["repo1", "repo2", "repo3"])

        # Check that the _public_repos_url method was called once
        mock_public_repos_url.assert_called_once()

        # Check that the get_json method was called once with the expected URL
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")  # noqa: E501


if __name__ == "__main__":
    unittest.main()
