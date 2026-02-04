import click
from .git_utils import get_staged_changes, is_git_repo

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
    click.echo(diff)

@main.command()
def pr():
    click.echo('Creating PR description...')

if __name__ == '__main__':
    main()