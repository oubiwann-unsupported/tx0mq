"""
Tests for L{tx0mq.factory}.
"""
from twisted.trial import unittest

from tx0mq.factory import ZmqFactory


class ZmqFactoryTestCase(unittest.TestCase):
    """
    Test case for L{zmq.twisted.factory.Factory}.
    """

    def setUp(self):
        self.factory = ZmqFactory()

    def test_shutdown(self):
        self.factory.shutdown()
