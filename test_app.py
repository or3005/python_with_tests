import pytest
from app import fetch_url

def test_fetch_url():
    assert fetch_url("https://www.google.com") == 200
