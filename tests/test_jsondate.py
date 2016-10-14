import datetime
import json
import unittest
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import jsondate


class JSONDateTests(unittest.TestCase):
    def assertTypeAndValue(self, expected_type, expected_value, result):
        self.assertIsInstance(result, expected_type)
        self.assertEqual(expected_value, result)

    def test_dumps_empty_roundtrips(self):
        self.assertEqual({}, jsondate.loads(jsondate.dumps({})))

    def test_dumps_str_roundtrips(self):
        # Generates a ValueError from _datetime_object_hook
        orig_dict = dict(foo='bar')
        self.assertEqual(orig_dict, jsondate.loads(jsondate.dumps(orig_dict)))

    def test_dump_unicode_roundtrips(self):
        orig_dict = {u'foo': u'bar', 'empty': u''}

    def test_dumps_none_roundtrips(self):
        # Generates a TypeError from _datetime_object_hook
        orig_dict = dict(foo=None)
        self.assertEqual(orig_dict, jsondate.loads(jsondate.dumps(orig_dict)))

    def test_dumps_datetime_roundtrips(self):
        orig_dict = dict(created_at=datetime.datetime(2011, 1, 1))
        self.assertEqual(orig_dict, jsondate.loads(jsondate.dumps(orig_dict)))

    def test_dumps_date_roundtrips(self):
        orig_dict = dict(created_at=datetime.date(2011, 1, 1))
        self.assertEqual(orig_dict, jsondate.loads(jsondate.dumps(orig_dict)))

    def test_dumps_datelike_string_does_not_roundtrip(self):
        """A string that looks like a date *will* be interpreted as a date.

        If for whatever reason, you don't want that to happen, you'll need to
        do some pre or post-processing to fixup the results.
        """
        orig_dict = dict(created_at='2011-01-01')
        expected = dict(created_at=datetime.date(2011, 1, 1))
        self.assertEqual(expected, jsondate.loads(jsondate.dumps(orig_dict)))

    def test_dump_datetime_roundtrips(self):
        orig_dict = dict(created_at=datetime.date(2011, 1, 1))
        fileobj = StringIO()
        jsondate.dump(orig_dict, fileobj)
        fileobj.seek(0)
        self.assertEqual(orig_dict, jsondate.load(fileobj))

    def test_unexpected_type_raises(self):
        dict_ = {'foo': set(['a'])}
        with self.assertRaises(TypeError):
            jsondate.dumps(dict_)

    def test_datetime_milliseconds(self):
        orig_dict = {
            'created_at': datetime.datetime(2016, 10, 14, 22, 12, 30, 123456)
        }
        should = '{"created_at": "2016-10-14T22:12:30:123456Z"}'
        is_value = jsondate.dumps(orig_dict)
        self.assertEqual(should, is_value)

