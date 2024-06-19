import click

@click.command()
@click.option('--output-dir', type=click.Path(), help='Specify the directory where the backup will be saved.')
@click.option('--compress', is_flag=True, help='Compress the backup file.')
@click.option('--label', help='Add a label to the backup for easier identification.')
@click.option('--retention', type=int, help='Set the number of days to keep the backup.')
def backup(output_dir, compress, label, retention):
    """Create a new backup of the PostgreSQL database."""
    # 여기에 백업 로직을 추가하세요
    click.echo(f"Creating backup... Output directory: {output_dir}, Compress: {compress}, Label: {label}, Retention: {retention} days")
