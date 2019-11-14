import os

def comparator (file1, file2):
    f1 = open(file1, 'r')
    f2 = open (file2, 'r')
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    for x in range(max(len(lines1), len(lines2))):
        if lines1[x] == lines2[x]:
            pass
        else:
            print("the file is modified at line number", x+1)
            break

comparator('./README.md', './server.py')
