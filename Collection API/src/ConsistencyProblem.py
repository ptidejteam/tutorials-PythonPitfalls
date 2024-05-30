import unittest


class Test(unittest.TestCase):

    def testGetWithDictionary(self):
        some_dict = {}
        some_dict['foo'] = { 'bar': 2 }
        value = some_dict.get('foo', {}).get('bar', {})

        self.assertEqual(value, 2)

    def testGetWithList(self):
        some_dict = {}
        some_dict['foo'] = { 'bar': [1, 2, 3] }
        value = some_dict.get('foo', {}).get('bar', []).get(1)

        self.assertEqual(value, 2)

