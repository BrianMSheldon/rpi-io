"""REST API for Raspberry Pi GPIO."""

import logging

from tornado.ioloop import IOLoop
from tornado.web import Application

from api import compat

# Configure logging
log = logging.getLogger()


def make_app():
    return Application()


def start(port: int = 8100):
    app = make_app()
    try:
        app.listen(port)
    except NotImplementedError:
        raise NotImplementedError('asyncio event loop policy may need to be set')
    IOLoop.current().start()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    compat.event_loop_policy()
    start()
