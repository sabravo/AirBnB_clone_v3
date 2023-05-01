#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
import time
from datetime import datetime, timedelta
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    def test_datetime_attributes(self):
        inst1 = BaseModel()
        time.sleep(0.1)  # wait for 0.1 seconds
        inst2 = BaseModel()
        tic = inst1.created_at
        toc = inst2.created_at
        self.assertNotEqual(tic, toc)


if __name__ == '__main__':
    unittest.main()
