from git import Repo, InvalidGitRepositoryError

def _get_repo():
    """Private helper to get the repo object. Returns None if not a git repo."""
    try:
        repo = Repo(search_parent_directories=True)
        if repo.bare:
            return None
        return repo
    except InvalidGitRepositoryError:
        return None
    
def is_git_repo():
    return _get_repo() is not None

def get_staged_changes():
    repo = _get_repo()
    if repo is None:
        return None
    staged_changes = repo.git.diff('--staged')
    return staged_changes

if __name__ == '__main__':
    print('Testing is_git_repo()...')
    result = is_git_repo()
    print(f"Is git repo: {result}")

    print('Getting staged changes...')
    print(f"Calling get_staged_changed: {get_staged_changes()}")