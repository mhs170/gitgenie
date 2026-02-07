from .git_utils import get_commit_log
from .llm_client import generate_text
def generate_pr_description(commits, base_branch='main'):
    commit_summary = ""
    for commit in commits:
        commit_summary += f"- {commit['hash']}: {commit['message']}\n"

    prompt = f"""You are an expert at writing GitHub Pull Request descriptions.

Based on the following commits, generate a comprehensive PR description.

Commits being merged into '{base_branch}':
{commit_summary}

Generate a PR description with this structure:

# [Title]
Brief one-line summary of the changes

## Description
2-3 sentences explaining what this PR does and why

## Changes
- Bullet point list of key changes
- Focus on what changed, not how
- Group related changes together

## Testing
Brief notes on how to test these changes (if applicable)

Use markdown formatting. Be clear and professional. Focus on what reviewers need to know.

Generate only the PR description, nothing else."""

    pr_description = generate_text(prompt)
    return pr_description
    

if __name__ == '__main__':
    commits = get_commit_log()
    if commits is None:
        print("Error: Could not get commits")
    elif not commits:
        print("No commits found between current branch and main")
    else:
        print(f"Found {len(commits)} commits\n")
        result = generate_pr_description(commits)
        if result:
            print("--- Generated PR Description ---")
            print(result)
        else:
            print("Error: Failed to generate PR description")