import click
from .git_utils import get_staged_changes, is_git_repo, get_commit_log
from .commit_analyzer import generate_commit_message
from .pr_generator import generate_pr_description

@click.group()
def main():
    """Main entry point for the GitGenie CLI."""
    if not is_git_repo():
        click.echo("Error: Not a git repository")
        raise click.Abort()

@main.command()
def commit():
    click.echo('Generating commit...')
    diff = get_staged_changes()
        
    if not diff:
        click.echo("Error: No staged changes")
        return
    commit_message = generate_commit_message(diff)
    if commit_message is None:
        click.echo('Error: Failed to generate commit message')
        return
    click.echo("\n--- Generated Commit Message ---")
    click.echo(commit_message)
    click.echo("--------------------------------\n")

@main.command()
def pr():
    click.echo('Generating PR description...')
    
    commits = get_commit_log()
    
    if commits is None:
        click.echo("Error: Could not get commit log")
        return
    
    if not commits:
        click.echo("No commits found between current branch and main")
        return
    
    click.echo(f"Found {len(commits)} commits\n")
    
    pr_description = generate_pr_description(commits)
    
    if pr_description is None:
        click.echo("Error: Failed to generate PR description")
        return
    
    click.echo("\n--- Generated PR Description ---")
    click.echo(pr_description)
    click.echo("--------------------------------\n")


if __name__ == '__main__':
    print('hello, world')
    main()