from pj_1.client_my import py_dumps_str_foo, tcp_sock_create


def test_py_dumps_str_foo():
    assert py_dumps_str_foo([]) == "[]"


def test_tcp_sock_create():
    assert tcp_sock_create()==""
