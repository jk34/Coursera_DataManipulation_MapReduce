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
    # key: order_id
    # value: elements/attributes
    #table = record[0] #table the record comes from, either "line_item" or "order"
    order_id = record[1] #order_id
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: order_id
    # value: elements/attributes
    lineitem_elements=[]
    order_elements=[]
    for row in list_of_values:
        if row[0] =="order":
            order_elements=row
        else:
            if order_elements: #checks if order_elements is non-empty or is empty
                lineitem_elements.append(row)
	#because the query is "WHERE Order.order_id = LineItem.order_id"
	#we append every "lineitem"" whose order_id matches that of a given "order"
	#thats why we use "append" for "lineitem_elements", but not for "order_elemenets"
	#it would be vice-versa is query were "WHERE LineItem.order_id = Order.order_id"
    for eachline in lineitem_elements:
        mr.emit(order_elements+eachline)
	#want to combine each lineitem to each order, one at a time
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
