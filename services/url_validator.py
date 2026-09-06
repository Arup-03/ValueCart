from urllib.parse import urlparse


def is_valid_url(url):
    try:
        result = urlparse(url)

        if result.scheme in ["http", "https"] and result.netloc:
            return True

        return False

    except Exception:
        return False