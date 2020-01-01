"""REST API for Raspberry Pi GPIO."""

import json
import logging

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler

from api import compat

# Configure logging
log = logging.getLogger()


class IndexHandler(RequestHandler):
    SUPPORTED_METHODS = ['GET']

    def get(self):
        index = {
            '/index': 'The API index',
        }
        self.write(json.dumps(index))


class RootHandler(RequestHandler):
    SUPPORTED_METHODS = ['GET']

    def get(self):
        shutdown = self.get_argument('shutdown')
        log.debug(f'Received shutdown argument: {shutdown!r}')
        if shutdown.lower() == 'true':
            self.write('Shutting down')
            log.warning('System shutdown initiated from api')
            raise SystemExit('Shutting down')


def make_app():
    return Application([
        ('/', RootHandler),
        ('/index', IndexHandler),
    ])


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
