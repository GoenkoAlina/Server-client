import socket
import threading
import time
import hamming


class Client:
	def __init__(self):
		self._server = ("192.168.3.4", 9090)
		#self._server = ("127.0.1.1", 9090)
		self._socket_TCP_IP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self._shutdown = False
		self.name = None

	def bind(self):
		self._socket_TCP_IP.bind(("192.168.3.5", 0))
		#self._socket_TCP_IP.bind(("192.168.3.4", 0))
		self._socket_TCP_IP.setblocking(0)

	def receive(self):
		while not self._shutdown:
			try:
				data, addr = self._socket_TCP_IP.recvfrom(1024)
				mess = data.decode("utf8")
				mess = mess.split(" ")
				print(mess[0], hamming.decode(mess[1]))
				time.sleep(0.2)
			except:
				pass

	def client_start(self):
		self.name = input("Name:")
		self._socket_TCP_IP.sendto(self.name.encode("utf-8"), self._server)
		while True:
			name = input()
			if name == "Exit":
				self._socket_TCP_IP.sendto(("Exit").encode("utf-8"), self._server)
				break
			message = input()
			if message != "":
				message = hamming.encode(message)
				self._socket_TCP_IP.sendto((name + " " + message).encode("utf-8"), self._server)
			time.sleep(0.2)
		self._shutdown = True

	def __del__(self):
		self._socket_TCP_IP.close()


def main():
	client = Client()
	client.bind()
	receive = threading.Thread(target=client.receive)
	receive.start()
	client.client_start()
	receive.join()


if __name__ == "__main__":
	main()
