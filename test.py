import os

for root,d_names,f_names in os.walk('.'):
    if(root == '.'):
	    print (root, d_names, f_names)