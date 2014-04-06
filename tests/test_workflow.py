import unittest
# import mock
from App.workflow import Error


class TestError(unittest.TestCase):
    def test_message(self):
        try:
            raise Error
        except Error as e:
            self.assertEqual(e.message, 'Workflow error occurred.')

        msg = 'OMG THINGS BROKE!!!!'
        try:
            raise Error(msg)
        except Error as e:
            self.assertEqual(e.message, msg)

    def test_str(self):
        try:
            raise Error
        except Error as e:
            self.assertEquals(str(e), 'Workflow error occurred.')