import socket
from _thread import *
import sys
from collections import deque
import pickle
import arcade
import random
import briscola_class

pixel_w=50 ## lunghezza base carta
rapp_xony=497/821 ## rapporto tra base ed altezza carta
pixel_h=pixel_w/rapp_xony
dist_card=4
pos_card=[1/4,3/4]
val_glob={1:"ace",
           2:"two",
           3:"three",
           4:"four",
           5:"five",
           6: "six",
           7:"seven",
           8:"jack",
           9:"horse",
           10:"king"}
suit_glob={"Denari":"g",
          "Coppe":"c",
          "Bastoni":"b",
          "Spade":"s"}
back=arcade.Sprite("sprite/briscola-cards/n_back.png")
back._set_scale(pixel_w/back._get_width())


sd=random.randint(0,1000)

print("seed server = ", sd)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
#pos = ["0:0,0,0,9,0,0,0,0,0", "1:0,0,0,9,0,0,0,0,0"]

#pos =[[0,[],0,9,0,[],[],deque(),[]],[0,[],0,9,0,[],[],deque(),[]]]
### seed,start,wait
pos= [[sd,0,9,0],[sd,0,9,0]]
def threaded_client(conn,player):
    global currentId, pos
    conn.send(pickle.dumps(pos[player]))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(65406824+1000)
            print("data = conn.recv")
            #reply = data.decode('utf-8')
            pos[player] = pickle.loads(data)
            print("player = ",player," pos = ",pos[player])
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: ", reply)
                #print("Recieved: ")

                #arr = reply.split(":")
                #id = int(arr[0])
                #pos[id] = reply
                #print("reply=",reply)
                if player == 0: reply = pos[1]
                if player == 1: reply = pos[0]

                #reply = pos[nid][:]
                print("Sending: ", reply)
                #print("Sending: ")

            #conn.sendall(str.encode(reply))
            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Connection Closed")
    conn.close()
player=0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,player))
    player+=1