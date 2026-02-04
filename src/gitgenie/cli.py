import click

@click.group()
def main():
    """Main entry point for the GitGenie CLI."""
    pass

@main.command()
def commit():
    click.echo('Generating commit...')

@main.command()
def pr():
    click.echo('Creating PR description...')

if __name__ == '__main__':
    main()