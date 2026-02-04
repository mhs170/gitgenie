import os
from git import Repo
from gitgenie.git_utils import is_git_repo


class TestIsGitRepo:
    """Test suite for is_git_repo function."""

    def test_is_git_repo_in_valid_repo(self, tmp_path):
        """Test that is_git_repo returns True when in a valid git repository."""
        # Create a git repo in temp directory
        repo = Repo.init(tmp_path)
        
        # Change to that directory
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            assert is_git_repo() is True
        finally:
            os.chdir(original_dir)

    def test_is_git_repo_in_subdirectory(self, tmp_path):
        """Test that is_git_repo returns True when in a subdirectory of a git repo."""
        # Create a git repo
        repo = Repo.init(tmp_path)
        
        # Create a subdirectory
        subdir = tmp_path / "subdir" / "nested"
        subdir.mkdir(parents=True)
        
        # Change to subdirectory
        original_dir = os.getcwd()
        try:
            os.chdir(subdir)
            assert is_git_repo() is True
        finally:
            os.chdir(original_dir)

    def test_is_git_repo_not_in_repo(self, tmp_path):
        """Test that is_git_repo returns False when not in a git repository."""
        # Create a regular directory (not a git repo)
        non_git_dir = tmp_path / "not_a_repo"
        non_git_dir.mkdir()
        
        original_dir = os.getcwd()
        try:
            os.chdir(non_git_dir)
            assert is_git_repo() is False
        finally:
            os.chdir(original_dir)

    def test_is_git_repo_in_bare_repo(self, tmp_path):
        """Test that is_git_repo returns False for bare repositories."""
        # Create a bare repository
        bare_repo = Repo.init(tmp_path, bare=True)
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            assert is_git_repo() is False
        finally:
            os.chdir(original_dir)

    def test_is_git_repo_with_commits(self, tmp_path):
        """Test that is_git_repo works in a repo with commits."""
        # Create a git repo with a commit
        repo = Repo.init(tmp_path)
        
        # Create a file and commit
        test_file = tmp_path / "test.txt"
        test_file.write_text("test content")
        repo.index.add(["test.txt"])
        repo.index.commit("Initial commit")
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            assert is_git_repo() is True
        finally:
            os.chdir(original_dir)