import socket                   # Import socket module
import os

filelist = str()
             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.





for root,d_names,f_names in os.walk('.'):
    if(root == '.'):
        for i in f_names:
            g = open(i)
            contents = str()
            contents = i + "|" + g.read()
            print(contents)
            s = socket.socket()
            s.connect((host, port))
            s.send(contents)
            with open('received_file', 'wb') as f:
                print ('file opened')
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

s = socket.socket()
s.connect((host, port))
s.send("Done")

f=open("received_file", "r")

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