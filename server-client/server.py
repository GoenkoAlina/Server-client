import socket
import re


class Server:
    def __init__(self):
        # self._ip = "192.168.3.4"
        self._ip = "127.0.1.1"
        self._port = 9090
        self._clients = {}
        self._online = {}
        self._names = {}
        self._socket_TCP_IP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def bind(self):
        self._socket_TCP_IP.bind((self._ip, self._port))

    def server_start(self):
        print("Server started!")
        print(f"Server IP: {self._ip} port: {self._port}")

        pattern = re.compile(r'\w+')

        while True:
            try:
                data, address = self._socket_TCP_IP.recvfrom(1024)

                if address not in self._names:
                    self._names[address] = data.decode("utf8")
                    self._clients[data.decode("utf8")] = address
                    self._online[address[1]] = True
                    print(f"id: {address[1]} <=> name: {data.decode('utf8')} is online!")
                    continue

                if self._online[address[1]] == False:
                    self._online[address[1]] = True

                data = data.decode("utf8")
                name = pattern.findall(data)[0]
                data = data[len(name) + 1:]

                if name == 'Exit':
                    self._online[address[1]] = False
                    print(f"id: {address[1]} <=> name: {self._names[address]} left the chat!")

                elif name in self._clients:
                    if self._online[self._clients[name][1]]:
                        self._socket_TCP_IP.sendto(f"{self._names[address]}: {data}".encode("utf8"), self._clients[name])
                        print(f"{address[1]} sent {self._clients[name][1]} a message!")
                    else:
                        self._socket_TCP_IP.sendto(f"user {name} is offline!".encode("utf8"), address)
                        print(f"user {name} is offline!")
                else:
                    self._socket_TCP_IP.sendto(f"user {name} is not registered!".encode("utf8"), address)
                    print(f"user {name} is not registered!")
            except:
                print("\nThe server stopped!")
                break

    def __del__(self):
        self._socket_TCP_IP.close()


def main():
    server = Server()
    server.bind()
    server.server_start()


if __name__ == "__main__":
    main()
