#!/usr/bin/env python
import logging
import os
import sys
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader

source = "./templates"
destination = "./static/apps"
environment = Environment(loader=FileSystemLoader(os.path.join(source)))

logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)


def main():
    path = "productlist/assets/js/productlist.js"
    template = environment.get_template(path)

    log.warning(f"Rendering {path}")
    content = template.render(server_url=os.getenv("server_url"))
    with open(os.path.join(destination, path), mode="w") as file:
        file.write(content)

    log.warning("All templates are rendered")


def run_server():
    port = 9000
    server_address = ("", port)

    log.warning(f"Server is running on port {port}")
    httpd = ThreadingHTTPServer(server_address, partial(SimpleHTTPRequestHandler, directory="static/apps"))
    httpd.serve_forever()


if __name__ == '__main__':
    main()
    run_server()

