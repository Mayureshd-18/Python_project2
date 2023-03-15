from project import chooser,decrypt,encrypt
import pytest
import unittest.mock
import builtins

def test_decrypt():
    assert decrypt("-.. . . -..") == "DEED"

def test_encrypt():
    assert encrypt("DEEG") == "-.. . . --. "

def test_chooser():
     with unittest.mock.patch.object(builtins, 'input', lambda _: '1'):
        assert chooser() == '1'