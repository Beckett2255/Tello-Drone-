# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


def firstHoop():
    sendmsg("up 100")
    sendmsg("forward 200")

    sendmsg("forward 300")


"""
# def secondHoop():

def secondHoop():
     sendmsg("up 100")
     sendmsg("forward 100")
# def thirdHoop():


# def fourthHop(): 
#D8DE1F
    sendmsg("up 100")
    sendmsg("forward 40")
    sendmsg("ccw 90")
    sendmsg("forward 50")
    sendmsg(cw 90")

#D8DE1F    
"""

print("\nTeam: Krueger and Jacobs")
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('takeoff')

        # Review the (SDK) Software Development Kit resource for Drone Commands
        # Delete these comments before writing your program

        sendmsg('land')

        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()
sock.close() 