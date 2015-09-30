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
    # key: document identifier, document_id
    # value: document text
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of document_id's
    list_doc_id=[]
    for v in list_of_values:
        if v not in list_doc_id: #so you don't have duplicate doc_id's in the list
            list_doc_id.append(v)
    mr.emit((key, list_doc_id))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
