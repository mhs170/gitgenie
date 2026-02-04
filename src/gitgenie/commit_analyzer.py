from .git_utils import get_staged_changes
from .llm_client import generate_text

def generate_commit_message(diff):
    prompt = f"""You are an expert at writing git commit messages following the Conventional Commits specification.

Analyze the following git diff and generate a clear, concise commit message.

Rules:
1. Use the format: type(scope): description
2. Types: feat, fix, docs, style, refactor, test, chore, perf
3. Keep the description under 72 characters
4. Use imperative mood (e.g., "add" not "added" or "adds")
5. Be specific about what changed
6. Don't include file paths in the message

Examples:
- feat(auth): add JWT token validation
- fix(api): resolve null pointer in user endpoint
- docs(readme): update installation instructions
- refactor(utils): simplify date formatting logic

Git diff:
{diff}

Generate only the commit message, nothing else. No explanation, no code blocks, just the commit message."""

    return generate_text(prompt)

if __name__ == '__main__':
    diff = get_staged_changes()
    if diff is None:
        print("Error: Not a git repository")
    elif not diff:
        print("Error: No staged changes")
    else:
        result = generate_commit_message(diff)
        if result:
            print(f"Generated message: {result}")
        else:
            print("Error: Failed to generate message")