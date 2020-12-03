import numpy as np
import os

cwd = os.getcwd()
file_loc = cwd + '\input.txt'
data = np.loadtxt(file_loc,dtype=str,delimiter=None,comments=None)

split_data = []
for i in range(len(data)):
    split_data.append(list(data[i]))
split_data = np.array(split_data)

rlimit = len(split_data[0])
vlimit = len(split_data)

#go right 3 down 1
trees= 0     
i = 0
j = 0
while i < vlimit: # think this works with indexing because we want to go once over
    if split_data[i,j] == '#':
        trees += 1
    j = j+3 if j+3 <= rlimit-1 else 3-(rlimit-j) # needs to be 2 
    i+=1
print(trees)

### part two ###

rights = np.array([1,3,5,7,1])
downs = np.array([1,1,1,1,2])
tree_list = []
for k in range(len(rights)):
    i = 0
    j = 0
    trees = 0
    deli = downs[k]
    delj = rights[k]
    while i < vlimit: # think this works with indexing because we want to go once over
        if split_data[i,j] == '#':
            trees += 1
        j = j+delj if j+delj <= rlimit-1 else delj-(rlimit-j) # needs to be 2 
        i+=deli
    tree_list.append(trees)

print(tree_list, np.prod(np.array(tree_list, dtype=float)))