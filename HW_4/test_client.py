import unittest
import client
import time
import argparse
import pickle


presence = {
    "action": 'presence',
    "time": time.ctime(time.time()),
    "type": "status",
    "user": {
        "account_name": 'User',
        "status": "Yep, I am here!"
    }
}


class TestSalary(unittest.TestCase):

    def test_create_parser(self):
        parser = argparse.ArgumentParser()
        self.assertEqual(type(client.create_parser()), type(parser))

    def test_make_presence(self):
        self.assertEqual(client.make_presence(), (presence))

    def test_send_presence(self):
        data = {'one': 1}
        data = pickle.dumps(data)
        self.assertEqual(client.send_presence({'one': 1}), data)

    def test_get_response(self):
        response = pickle.dumps({'response': 'data', 'alert': 'Вы на сервере'})
        self.assertEqual(client.get_response(response), ('Вы на сервере'))

    if __name__ == "__main__":
        unittest.main()
