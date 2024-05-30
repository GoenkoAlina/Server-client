from server import Server
from client import Client
import threading
import unittest
import time


class UnitTests(unittest.TestCase):
    def test_name(self):
        self.assertEqual('Alina', 'Alina')


def main():
    unittest.main()

# def main():
#     server = Server()
#     server.bind()
#     server.server_start()

# def main():
# 	client = Client()
# 	client.bind()
# 	receive = threading.Thread(target=client.receive)
# 	receive.start()
# 	client.client_start()
# 	receive.join()


if __name__ == "__main__":
    main()
