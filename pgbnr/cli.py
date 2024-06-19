import click
from pgbnr.commands.backup import backup
from pgbnr.commands.restore import restore
from pgbnr.commands.replicate import replicate
from pgbnr.commands.status import status
from pgbnr.commands.schedule import schedule
from pgbnr import config

@click.group()
@click.version_option("1.0.0", "-v", "--version")
@click.option('-c', '--config', type=click.Path(), help='Specify the configuration file to use.')
@click.option('-l', '--log-level', default='info', type=click.Choice(['debug', 'info', 'warning', 'error', 'critical']), help='Set the log level. Default is info.')
@click.option('-d', '--dry-run', is_flag=True, help='Show what would have been done without making any changes.')
@click.pass_context
def cli(ctx, config, log_level, dry_run):
    """pgbnr: PostgreSQL Backup and Replication Management Tool"""
    ctx.ensure_object(dict)
    ctx.obj['CONFIG'] = config
    ctx.obj['LOG_LEVEL'] = log_level
    ctx.obj['DRY_RUN'] = dry_run

cli.add_command(backup)
cli.add_command(restore)
cli.add_command(replicate)
cli.add_command(status)
cli.add_command(schedule)

if __name__ == '__main__':
    cli()
