# Tuples are ordered sequence of elements contained by parentheses 
# and separated by commas
(10, 9, 5, 7, 2, 6)
(5.6, 87.8, 8.7, 9.1, 2.3)
tuple1 = ('first', 'second', 'third')

# Tuples can contain mixed types
('Michael', 10, 'Thriller', 0.5, True)

# Tuple elements can be get by indexed
tuple1[0]  # it's equal to 'first'
('first', 'second', 'third')[2]  # it's equal to 'third'
('first', 'second', 'third')[-1] # it's equal to 'third'

# Combine tuples result in a sequence of then
tuple1 + (10, 9, 5, 7, 2, 6) # it's equal to ('first', 'second', 'third', 10, 9, 5, 7, 2, 6)

# Subtuples can be get using a index interval
# from the inicial element to the last (not included)
tuple1[0:2] # it's equal to ('first', 'second')
tuple1[1:3] # it's equal to ('second', 'third')

# Get every element on a set interval
tuple1[::2] # it's equal to ('first', 'third')

# Get the lenght of a tuple
len(tuple1)              # it returns 3
len((10, 9, 5, 7, 2, 6)) # it returns 6

# Sort the elements of a tuple
sorted((5,4,7,1))                 # it returns [1, 4, 5, 7] ## NOTE: the sorted return is a list, not a tuple
sorted((5,4,7,1), reverse = True) # it returns [7, 5, 4, 1] ## NOTE: the sorted return is a list, not a tuple

# Tuples elements can be other tuples
tuple2 = (1, 2, ('nesting', 'tuple'), (2.4), (5, (4, 0)))
tuple2[0]         # it's equal to 1
tuple2[2]         # it's equal to ('nesting', 'tuple')
tuple2[2][1][1:4] # it's equal to 'upl'
tuple2[4][1]      # it's equal to (4, 0)
