import os
from unittest import TestCase

from .data import read_ulog

LOG_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    os.path.pardir,
    'logs')


class TestData(TestCase):
    def test_read_ulog(self):
        data = read_ulog(
            log_path=os.path.join(
                LOG_DIR,
                '015b95dc-27a1-437d-999e-a3d5db383821.ulg'),
            message_list=None)
        self.assertIsNotNone(data)
