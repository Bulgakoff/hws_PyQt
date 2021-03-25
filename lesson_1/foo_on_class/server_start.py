import click
from foo_on_class.server_my \
    import current_start_server





# ==========click=====server=======
@click.command()
@click.argument('addr')
@click.argument('port')
def main(addr, port):
    current_start_server(addr, port)


if __name__ == '__main__':
    main()