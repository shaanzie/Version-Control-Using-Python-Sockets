# import socket                   # Import socket module

# s = socket.socket()             # Create a socket object
# host = socket.gethostname()     # Get local machine name
# port = 6002                    # Reserve a port for your service.

# file = './README.md'
# s.connect((host, port))
# f = open(file, 'r')
# contents = f.read()
# s.send(contents)
# f.close()

# with open('received_file', 'wb') as f:
#     print ('file opened')
#     while True:
#         print('receiving data...')
#         data = s.recv(1024)
#         print('data=', (data))
#         if not data:
#             break
#         # write data to a file
#         f.write(data)

# f.close()
# s.close()

import socket                   # Import socket module
import os

filelist = str()
             # Create a socket object
host = "192.168.43.76"     # Get local machine name
port = 6008                    # Reserve a port for your service.





for root,d_names,f_names in os.walk('./cl'):
        for i in f_names:
            # i = 'README.md'
            g = open("./cl/"+i)
            print(i)
            contents = str()
            contents = i + "|" + g.read()
            print(contents)
            s = socket.socket()
            s.connect((host, port))
            s.send(contents)
            with open('./cl/received_file', 'wb') as f:
                # print ('file opened')
                while True:
                    print('receiving data...')
                    data = s.recv(10000)
                    if not data:
                        break
                    # write data to a file
                    f.write(data)
            s.close()
            g.close()
            f.close()

# s = socket.socket()
# s.connect((host, port))
# s.send("Done")

f=open("./cl/received_file", "r")

if f.mode == 'r':
    contents = f.read()

if(len(contents)!=0):
    print(contents)
else:
    print("No changes, safe to commit")

f.close()

print('Successfully get the file')
s.close()
print('connection closed')