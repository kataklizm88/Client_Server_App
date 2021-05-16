import unittest
import server
import argparse
import time
import pickle


parser = argparse.ArgumentParser()
example = {
        "action": 'presence',
        "time": time.ctime(time.time()),
        "type": "status",
        "user": {
                "account_name":  'name',
                "status":      "Yep, I am here!"
                }
        }


class TestSalary(unittest.TestCase):

    def test_create_parser(self):
        self.assertEqual(type(server.create_parser()), type(parser))

    def test_get_message(self):

        self.assertEqual(server.get_message(), ('Ничего'))

    def test_prepare_response(self):
        self.assertEqual(server.prepare_response(example), (200))

    def test_send_response(self):
        response = pickle.dumps({'response': 'data', 'alert': 'Вы на сервере'})
        self.assertEqual(server.send_response('data'), (response))

    if __name__ == "__main__":
        unittest.main()