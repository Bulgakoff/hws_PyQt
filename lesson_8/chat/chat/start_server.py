import click


@click.command()
@click.option("--address", required=True)
@click.option("--port", required=True, type=int)
def start(address, port):
    print(f"start server {address}:{port}")
