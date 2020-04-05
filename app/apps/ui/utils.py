
def parse_url(url):
    """Remove locale from url and return it
    """
    url = str(url).replace("/en/", "/")
    url = str(url).replace("/fr/", "/")
    url = str(url).replace("/es/", "/")

    return url