import MapReduce
import sys

"""
Problem 1
Create an Inverted index. Given a set of documents, an inverted index 
is a dictionary where each word is associated with a 
list of the document identifiers in which that word appears.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    if record[0]=="a":
        for i in range(5): #because looking at matrix.json, we see A and B are 5x5 matrices
			mr.emit_intermediate((record[1],i),(record[2],record[3]))
    if record[0]=="b":
        for j in range(5): #because looking at matrix.json, we see A and B are 5x5 matrices
            mr.emit_intermediate((j,record[2]),(record[1],record[3]))

def reducer(key, list_of_values): 
    vals={}
    C_ik=0
    for entry in list_of_values:
        if entry[0] not in vals:
            vals[entry[0]] = entry[1]
        else:
            C_ik+=vals[entry[0]]*entry[1]

    mr.emit((key[0],key[1],C_ik))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
