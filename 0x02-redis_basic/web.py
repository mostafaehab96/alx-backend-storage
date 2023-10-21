#!/usr/bin/env python3
""" implement a get_page function."""

import requests
import redis


def get_page(url: str) -> str:
    """
    obtain the HTML content of a particular URL and returns it
    :param url: the url to obtain it's HTML
    :return: HTML content
    """
    client = redis.Redis()
    client.incr(f'count:{url}')
    response = requests.get(url, allow_redirects=True, timeout=30)
    cached_page = client.get(f'{url}')
    if cached_page:
        return cached_page.decode('utf-8')
    if response.status_code == 200:
        client.set(f'{url}', response.text, 10)
        return response.text
