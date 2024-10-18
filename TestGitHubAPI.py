import unittest
from unittest.mock import patch
import requests

# Assuming the function is defined in a module named github_api
from GitHubAPI import get_user_repos_and_commits

class TestGitHubAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_user_repos_and_commits_success(self, mock_get):
        # Mock response for the repositories endpoint
        mock_repos_response = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get.side_effect = [
            # Mock the response for the user's repositories request
            unittest.mock.Mock(status_code=200, json=lambda: mock_repos_response),
            # Mock the response for the commits request for "repo1"
            unittest.mock.Mock(status_code=200, json=lambda: [{"commit": {}}] * 5),
            # Mock the response for the commits request for "repo2"
            unittest.mock.Mock(status_code=200, json=lambda: [{"commit": {}}] * 3)
        ]
        
        # Capture the printed output
        with unittest.mock.patch('builtins.print') as mocked_print:
            get_user_repos_and_commits("testuser")
            
            # Verify that the expected output was printed
            mocked_print.assert_any_call("Repo: repo1 Number of commits: 5")
            mocked_print.assert_any_call("Repo: repo2 Number of commits: 3")

    @patch('requests.get')
    def test_get_user_repos_and_commits_no_repos(self, mock_get):
        # Mock an empty response for the repositories endpoint
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: []),  # No repos
        ]
        
        with unittest.mock.patch('builtins.print') as mocked_print:
            get_user_repos_and_commits("testuser")
            
            # Ensure no output, as there are no repositories
            mocked_print.assert_not_called()

    @patch('requests.get')
    def test_get_user_repos_and_commits_failed_repo_request(self, mock_get):
        # Mock a failed response for the repositories request
        mock_get.return_value = unittest.mock.Mock(status_code=404)
        
        with unittest.mock.patch('builtins.print') as mocked_print:
            get_user_repos_and_commits("testuser")
            
            # Verify the error message was printed
            mocked_print.assert_called_with("Failed to retrieve repositories for user: testuser")

    @patch('requests.get')
    def test_get_user_repos_and_commits_failed_commits_request(self, mock_get):
        # Mock response for the repositories endpoint
        mock_repos_response = [
            {"name": "repo1"}
        ]
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: mock_repos_response),
            unittest.mock.Mock(status_code=404)  # Mock failed commit retrieval
        ]
        
        with unittest.mock.patch('builtins.print') as mocked_print:
            get_user_repos_and_commits("testuser")
            
            # Verify the error message for the failed commits request
            mocked_print.assert_called_with("Failed to retrieve commits for repo: repo1")

if __name__ == '__main__':
    unittest.main()
