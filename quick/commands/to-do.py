import click


class Context:
    def __init__(self, priority):
        self.priority = priority


@click.group()
@click.option("-p", "--priority", type=str, help="1 to sort by priority")
@click.pass_context
def cli(ctx, priority):
    """To-Do list"""
    ctx.obj = Context( priority)

@cli.command()
@click.pass_context
def list(ctx):
    click.echo( f"Sort by priority={ctx.obj.priority}")

@cli.command()
@click.pass_context
def add(ctx):
    pass