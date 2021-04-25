def host_ping(addr) -> bool:
    pass


def host_range_ping(addresses, host_ping_fn):
    for addr in addresses:
        host_ping_fn(addr)


# code:
host_range_ping([...], host_ping)

# tests
host_ping_mock = MagicMock()
host_range_ping([...], host_ping_mock)
...
