import pyfirmata
import time
import os
import socketio

board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()
board.digital[10].mode = pyfirmata.INPUT

sis = socketio.SimpleClient()
sis.connect("http://192.168.0.100:3000")



while True:
    sw = board.digital[10].read()
    if sw is True:
        print("Button Pressed")
        sis.emit("newMessage", "Hello from Arduino")
        time.sleep(0.2)


