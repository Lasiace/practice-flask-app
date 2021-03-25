from flask import request, redirect, abort, url_for
from urllib.parse import urlparse, urljoin

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

def redirect_on_complete(on_complete = None):
    if on_complete:
        if not is_safe_url(on_complete):
            return abort(400)
        return redirect(on_complete)
    return redirect(url_for("index"))