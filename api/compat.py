"""
This module handles various compatibility issues.
"""

import asyncio
import logging
import sys

import tornado

# Configure logging
log = logging.getLogger()


def event_loop_policy():
    """Set the event loop policy."""
    windows_event_loop_policy()


def windows_event_loop_policy():
    """Set the asyncio event loop policy for Windows."""

    # On Windows with Python 3.8 and Tornado 5+ a "selector" event loop is required
    # Reference:
    #     https://github.com/tornadoweb/tornado/issues/2608

    if all([
        sys.platform == 'win32',
        sys.version_info >= (3, 8),
        tornado.version_info >= (5,),
    ]):
        policy = asyncio.WindowsSelectorEventLoopPolicy()
        log.debug('Configuring event loop policy')
        asyncio.set_event_loop_policy(policy)
