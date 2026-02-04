from git import Repo, InvalidGitRepositoryError

def is_git_repo():
    try:
        repo = Repo(search_parent_directories=True)
        if repo.bare:
            return False
        return True
    except InvalidGitRepositoryError:
        return False

if __name__ == '__main__':
    print('Testing is_git_repo()...')
    result = is_git_repo()
    print(f"Is git repo: {result}")