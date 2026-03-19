# Change your socket program, so that it counts the
# number of characters, it has received, and stops
# displaying any text, after it has shown 3000
# characters.

# The program should retrieve the entire document,
# count the total number of characters, and display
# the count, of the number of characteers, at the end
# of the document.

import socket

try:
    url = input("Enter a URL: ")

    split_url = url.split("/")

    host = split_url[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    convert_to_utf_8 = cmd.encode()
    mysock.send(convert_to_utf_8)

    byte_string = b""

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        byte_string += data
        
    byte_string = byte_string.decode()
    print(byte_string[:3000])
    print(len(byte_string))

    mysock.close()
except:
    print("Invalid URL.")
