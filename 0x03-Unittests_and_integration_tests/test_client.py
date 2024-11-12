import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
'''Test client module'''


class TestGithubOrgClient(unittest.TestCase):
    '''Tests for the GithubOrgClient.org method.'''

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        '''Test that GithubOrgClient.org returns the correct value.'''
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")  # noqa: E501
        self.assertEqual(result, {"login": org_name})

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        '''Test that the _public_repos_url method returns the correct URL.'''
        mock_org.return_value = {
            "login": "google",
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")
        mock_org.assert_called_once()

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)  # noqa: E501
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        '''Test that the public_repos method
        returns the correct repositories list.'''
        mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"  # noqa: E501
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}, {"name": "repo3"}]  # noqa: E501
        client = GithubOrgClient("google")
        repos = client.public_repos()
        self.assertEqual(repos, ["repo1", "repo2", "repo3"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")  # noqa: E501


if __name__ == "__main__":
    unittest.main()
