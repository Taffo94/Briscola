import socket
import pickle

class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost" # For this to work on your machine this must be equal to the ipv4 address of the machine running the server
                                    # You can find this address by typing ipconfig in CMD and copying the ipv4 address. Again this must be the servers
                                    # ipv4 address. This feild will be the same for all your clients.
        self.port = 5555
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def getid(self):
        return self.id

    def connect(self):
        self.client.connect(self.addr)
        #return self.client.recv(2048).decode()
        return pickle.loads(self.client.recv(65406824+1000))
    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            #print( "entro su send di network")
            #self.client.send(str.encode(data))
            self.client.send(pickle.dumps(data))
            #print("pickle.dumps(data) in network =")
            #print("len(data) = ",len(pickle.dumps(data)))
            #print("pickle.dumps(data)",pickle.dumps(data))
            #reply = self.client.recv(2048).decode()
            #print("self.client.recv(2048)")
            reply = pickle.loads(self.client.recv(65406824+1000))
            #print("reply = ",reply)
            return reply
        except socket.error as e:
            return str(e)
