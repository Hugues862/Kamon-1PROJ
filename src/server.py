import os
import pickle
import shlex
import socket
import subprocess
import threading
from commun.serverData import serverData
from commun.network import *
import dotenv


def runServer():

    TB = 2048 * 2
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server = socket.gethostbyname(socket.gethostname())

    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    os.environ["SERVER_IP"] = server
    dotenv.set_key(dotenv_file, "SERVER_IP", os.environ["SERVER_IP"])

    port = 56669
    try:
        s.bind((server, port))
        print(f"Started server {server} on port {port}")
    except socket.error as e:
        str(e)

    s.listen()

    SRVDATA = serverData()

    USERS = []

    def threaded_client(conn, id):
        # Connection started

        global SRVDATA
        global USERS

        conn.send(pickle.dumps(id))
        conn.send(pickle.dumps(SRVDATA))
        # main connection loop
        while True:

            data = recv_data(conn)
            stock = pickle.loads(data)
            print(stock)
            ##print(data)
            # print("recieved")
            SRVDATA.game = stock
            SRVDATA.game.turnChange()
            data = pickle.dumps(SRVDATA)
            for user in USERS:
                send_data(user[0], data)
            print("sent")

        # connection ends
        USERS[id] == None
        conn.close()
        print("Connection closed")

    while True:
        try:
            if len(USERS) <= 20:
                conn, addr = s.accept()
                print("Connected to:", addr)
                # id = int(''.join(str(e) for e in [randint(0,9) for x in range(6)]))
                id = len(USERS)
                USERS.append([conn, addr, id])
                thread = threading.Thread(
                    group=None,
                    target=threaded_client,
                    name=f"Player{id}",
                    args=(conn, id),
                    kwargs={},
                )
                thread.start()
        except KeyboardInterrupt:
            print("\nClosing server")
            s.close()
            break
