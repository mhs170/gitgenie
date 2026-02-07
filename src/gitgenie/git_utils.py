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

def get_commit_log(main_branch_name='main'):
    repo = _get_repo()
    if repo is None:
        return None
    try:
        feature_branch = repo.active_branch.name
        commits_unique_to_feature_branch = list(repo.iter_commits(f"{main_branch_name}..{feature_branch}"))
        commit_list = []
        for commit in commits_unique_to_feature_branch:
            commit_list.append({
                'hash': commit.hexsha[:7],
                'message': commit.message.strip(),
                'author': commit.author.name,
                'date': commit.committed_datetime.isoformat(),
            })
        return commit_list
    except Exception:
        return None


if __name__ == '__main__':
    print('Testing is_git_repo()...')
    result = is_git_repo()
    print(f"Is git repo: {result}")

    print('Getting staged changes...')
    print(f"Calling get_staged_changed: {get_staged_changes()}")

    print("Testing get_commit_log()")
    commits = get_commit_log()
    if commits is None:
        print("Error getting commits")
    elif not commits:
        print(" No commits (already on main/up to date)")
    else:
        print(f"Found {len(commits)} commits")
        for commit in commits[:3]:
            print(f"    - {commit['hash']}: {commit['message'][:50]}")