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
    nucleotide_seq = record[1] 
    nucleotide_seq=nucleotide_seq[:-10] #remove last 10chars
    mr.emit_intermediate(nucleotide_seq,1)

def reducer(key, list_of_values):
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
