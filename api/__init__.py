"""REST API for Raspberry Pi GPIO."""

import logging

from tornado.ioloop import IOLoop
from tornado.web import Application

# Configure logging
log = logging.getLogger()


def make_app():
    return Application()


def start(port: int = 8100):
    app = make_app()
    app.listen(port)
    IOLoop.current().start()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    start()
