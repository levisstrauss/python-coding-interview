from curses.ascii import isdigit
import findstring
import pytest


def test_ispresent():
    assert findstring.ispresent("N7")


def test_nodigit():
    assert findstring.nodigit("N7")