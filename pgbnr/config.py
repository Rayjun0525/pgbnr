import click

@click.group()
def config():
    """Manage pgbnr configuration settings."""
    pass

@config.command()
@click.argument('key')
@click.argument('value')
def set(key, value):
    """Set a configuration key to a new value."""
    # 여기에 설정 저장 로직을 추가하세요
    click.echo(f"Setting config {key} to {value}")

@config.command()
@click.argument('key')
def get(key):
    """Get the current value of a configuration key."""
    # 여기에 설정 조회 로직을 추가하세요
    click.echo(f"Getting config value for {key}")

@config.command()
def list():
    """List all configuration keys and values."""
    # 여기에 설정 목록 로직을 추가하세요
    click.echo("Listing all configs...")
