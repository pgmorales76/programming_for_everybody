# Change the `socket` program, so that it only shows
# data after the headers, and a blank line, have been
# received.

# Remember that `recv` receives characters (newlines
# and all), not lines.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

byte_string = b""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    byte_string += data
        
byte_string = byte_string.split(b"\r\n\r\n")

byte_string = byte_string[1]

byte_string = byte_string.decode()

print(byte_string)

mysock.close()
