"""
python -m pytest test_addition.py
python3 -m pytest abc.py -v
pip3 install pytest

"""


import addition
import pytest


def test_add():
    assert addition.add(4, 5) == 9


def test_sub():
    assert addition.sub(4, 5) == -1
