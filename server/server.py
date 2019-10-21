import socket                   # Import socket module
import os
port = 6006                # Reserve a port for your service.
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
    data = conn.recv(10000)
    contents = data.split('|')
    lines1 = contents[1]
    localfile = open(contents[0], 'r')
    lines2 = localfile.readlines()
    for ele in lines2:
      s1 += ele
    print("reading file ", contents[0])
    for x in range(min(len(s1), len(lines1))):
         if s1[x] == lines1[x]:
            count += 1
            charc += 1
         else:
               print ("the file %s is modified at character number\n" % str(filecount), str(charc))
               with open("out.txt", "a") as text_file:
                  text_file.write("the file {0} is modified at character number {1} \n".format(str(filecount), (str(charc))))
               break
   #  print(count)
    if count == min(len(s1), len(lines1)):
       print ("the file %s is not modified\n" % str(filecount))
       with open("out.txt", "a") as text_file:
         text_file.write("the file %s is not modified\n" % str(filecount))
    ftoread = open('out.txt', 'r')
    l = ftoread.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',l)
       break
    ftoread.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()
s.close()