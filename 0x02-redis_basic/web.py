#!/usr/bin/env python3
""" implement a get_page function."""

import requests


def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL and returns it
    :param url: the url to obtain it's HTML
    :return: HTML content
    """
    response = requests.get(url, allow_redirects=True, timeout=30)
    if response.status_code == 200:
        return response.text
