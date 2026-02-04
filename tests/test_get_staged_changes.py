# tests/test_get_staged_changes.py
import os
from git import Repo
from gitgenie.git_utils import get_staged_changes


class TestGetStagedChanges:
    """Test suite for get_staged_changes function."""

    def test_get_staged_changes_with_no_changes(self, tmp_path):
        """Test that get_staged_changes returns empty string when nothing is staged."""
        # Create a git repo with initial commit
        repo = Repo.init(tmp_path)
        test_file = tmp_path / "test.txt"
        test_file.write_text("initial content")
        repo.index.add(["test.txt"])
        repo.index.commit("Initial commit")
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = get_staged_changes()
            assert result == ""
        finally:
            os.chdir(original_dir)

    def test_get_staged_changes_with_new_file(self, tmp_path):
        """Test get_staged_changes with a newly added file."""
        # Create a git repo with initial commit
        repo = Repo.init(tmp_path)
        test_file = tmp_path / "existing.txt"
        test_file.write_text("existing")
        repo.index.add(["existing.txt"])
        repo.index.commit("Initial commit")
        
        # Add a new file and stage it
        new_file = tmp_path / "new_file.txt"
        new_file.write_text("new content")
        repo.index.add(["new_file.txt"])
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = get_staged_changes()
            assert result != ""
            assert "new_file.txt" in result
            assert "+new content" in result
        finally:
            os.chdir(original_dir)

    def test_get_staged_changes_with_modified_file(self, tmp_path):
        """Test get_staged_changes with a modified file."""
        # Create a git repo with initial commit
        repo = Repo.init(tmp_path)
        test_file = tmp_path / "test.txt"
        test_file.write_text("original content")
        repo.index.add(["test.txt"])
        repo.index.commit("Initial commit")
        
        # Modify the file and stage it
        test_file.write_text("modified content")
        repo.index.add(["test.txt"])
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = get_staged_changes()
            assert result != ""
            assert "test.txt" in result
            assert "-original content" in result
            assert "+modified content" in result
        finally:
            os.chdir(original_dir)

    def test_get_staged_changes_with_deleted_file(self, tmp_path):
        """Test get_staged_changes with a deleted file."""
        # Create a git repo with initial commit
        repo = Repo.init(tmp_path)
        test_file = tmp_path / "to_delete.txt"
        test_file.write_text("will be deleted")
        repo.index.add(["to_delete.txt"])
        repo.index.commit("Initial commit")
        
        # Delete the file and stage the deletion
        test_file.unlink()
        repo.index.remove(["to_delete.txt"])
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = get_staged_changes()
            assert result != ""
            assert "to_delete.txt" in result
            assert "-will be deleted" in result
        finally:
            os.chdir(original_dir)

    def test_get_staged_changes_with_multiple_files(self, tmp_path):
        """Test get_staged_changes with multiple staged files."""
        # Create a git repo with initial commit
        repo = Repo.init(tmp_path)
        file1 = tmp_path / "file1.txt"
        file1.write_text("file 1 content")
        repo.index.add(["file1.txt"])
        repo.index.commit("Initial commit")
        
        # Add and modify multiple files
        file2 = tmp_path / "file2.txt"
        file2.write_text("file 2 content")
        file1.write_text("file 1 modified")
        repo.index.add(["file1.txt", "file2.txt"])
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = get_staged_changes()
            assert result != ""
            assert "file1.txt" in result
            assert "file2.txt" in result
        finally:
            os.chdir(original_dir)

    def test_get_staged_changes_not_in_repo(self, tmp_path):
        """Test that get_staged_changes returns None when not in a git repo."""
        # Create a regular directory (not a git repo)
        non_git_dir = tmp_path / "not_a_repo"
        non_git_dir.mkdir()
        
        original_dir = os.getcwd()
        try:
            os.chdir(non_git_dir)
            result = get_staged_changes()
            assert result is None
        finally:
            os.chdir(original_dir)

    def test_get_staged_changes_ignores_unstaged(self, tmp_path):
        """Test that get_staged_changes only returns staged changes, not unstaged."""
        # Create a git repo with initial commit
        repo = Repo.init(tmp_path)
        test_file = tmp_path / "test.txt"
        test_file.write_text("original")
        repo.index.add(["test.txt"])
        repo.index.commit("Initial commit")
        
        # Modify file but don't stage it
        test_file.write_text("unstaged changes")
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            result = get_staged_changes()
            assert result == ""  # Should be empty since nothing is staged
        finally:
            os.chdir(original_dir)