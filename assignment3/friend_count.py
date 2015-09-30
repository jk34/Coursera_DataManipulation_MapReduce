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
    person = record[0] 
    friend = record[1] 
    mr.emit_intermediate(person, friend)

def reducer(key, list_of_values):
    # key: order_id
    # value: elements/attributes
    num=0
    for f in list_of_values:
        num+=1
    mr.emit((key, num))
	#want to combine each lineitem to each order, one at a time
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
