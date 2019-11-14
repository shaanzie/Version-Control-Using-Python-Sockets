import socket                   # Import socket module
import os
port = 6008                # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')
contents = []
count = 0
charc = 0
filecount = 0
flag = True
while flag:
    s1 = ''
    charc = 0
    filecount += 1
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(10000).decode()
    contents = data.split('|')
    print("reading file ", contents[0])
    lines1 = contents[1]
    localfile = open(contents[0], 'w')
    localfile.write(lines1)
    with open("out.txt", "a") as text_file:
        text_file.write("File successfully pushed\n")
    ftoread = open('out.txt', 'r')
    l = ftoread.read(1024)
    while (l):
       conn.send(l.encode())
       print('Sent ',l)
       break
    ftoread.close()

    print('Done sending')
    conn.send('Thank you for connecting'.encode())
    conn.close()
s.close()