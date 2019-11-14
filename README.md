# Version-Control-Using-Python-Sockets

An implementation of version control using socket programming architectures.

Git, as a decentralised version control library is used for open-source development and serves also as a project management tool for various workflows existing in the world today.

The main principle of git is
1. Handle content in snapshots, one for each commit
2. Apply and rollback changes between two snapshots.

Our version of git is using socket programming architectures, where a server holds all the code contributed by developers working on the project. This solution is scalable to many users, as it provides a TCP interface to each user, to maintain concurrency between people working on the project.

This project is a very basic implementation of the same, where it only involves the processes of diff, pull and push, to demonstrate how sockets can be used to simulate the working of a very basic version control system. This mainly derives from how TCP handles the connrection between multiple users and a central server, and that is exploited by the use of sockets.

## Abstractions for simplicity

1. This implementation uses static IPs to reference the nodes
2. It only assumes the functions of diff, pull and push
3. It assumes all files to be stored in the same directory of the server

## Usability
1. This approach is scalable to any number of users, but no two users can access the server at the same time.
2. Parallelism is not exploited here, as this is just a basic workflow

## Recreation

### git diff

1. Client
Run `sudo python3 client-diff.py`

2. Server
Run `sudo python3 server-diff.py`

### git pull

1. Client : `sudo python3 client-pull.py`

2. Server : `sudo python3 server-pull.py`

### git push

1. Client : `sudo python3 client-push.py`

2. Server : `sudo python3 server-push.py`
