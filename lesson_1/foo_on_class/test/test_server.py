import unittest
from socket import *
import pytest

from pj_1.server_my import tcp_sock_create, py_dumps_str_foo,\
    bind_create_from_user, str_loads_dict_foo\
    , b_decode_str_foo


def test_tcp_sock_create():
    assert tcp_sock_create() == '<socket.socket fd=800, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>', "Не пустые места"


def test_py_dumps_str_foo():
    assert py_dumps_str_foo([
        {
            "response": 200,
            "alert": "An optional message/notification - Ok!"
        },
        {
            "response": 402,
            "error": "This could be 'wrong password' or 'no account with that name'"
        },
    ]) == [{"response": 200, "alert": "An optional message/notification - Ok!"},
           {"response": 402, "error": "This could be 'wrong password' or 'no account with that name'"}], 'sdfsdff'


def test_py_dumps_str_foo2():
    assert py_dumps_str_foo({}) == '{}'


def test_bind_create_from_user():
    assert bind_create_from_user('', "", "1111") == ''


def test_str_loads_dict_foo():
    assert str_loads_dict_foo('{"qwe":45}') == {"qwe": 45}


def test_b_decode_str_foo():
    assert b_decode_str_foo(b'asd') == 'asd'


