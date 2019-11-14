import socket                   # Import socket module
import os

filelist = str()                # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 6008                     # Reserve a port for your service.





for root,d_names,f_names in os.walk('./cl'):
        for i in f_names:
            
            g = open("./cl/"+i)
            print(i)
            contents = str()
            contents = i + "|" + g.read()
            print(contents)

            s = socket.socket()

            s.connect((host, port))

            s.send(contents.encode())

            with open('./cl/received_file', 'wb') as f:
                
                while True:
                    print('receiving data...')
                    data = s.recv(10000)
                    if not data:
                        break
                    
                    f.write(data)
            s.close()
            g.close()
            f.close()



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