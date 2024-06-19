import click

@click.command()
@click.option('--detailed', is_flag=True, help='Show detailed status information.')
def status(detailed):
    """Show the current status of backups and replication."""
    # 여기에 상태 확인 로직을 추가하세요
    click.echo(f"Showing status... Detailed: {detailed}")
