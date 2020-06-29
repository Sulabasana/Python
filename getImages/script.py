import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

    #urlparse() function parses a URL into six components, we just need to see if the netloc (domain name) and scheme (protocl) are there.

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
    # make the URL absolute by joining domain with the URL that is just extracted
    img_url = urljoin(url, img_url)
    try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
    except ValueError:
            pass