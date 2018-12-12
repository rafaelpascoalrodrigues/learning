# Lists are ordered sequence of elements contained by square brackets 
# and separated by commas
[5.6, 87.8, 8.7, 9.1, 2.3]
list1 = ['first', 'second', 'third']
list2 = [10, 9, 5, 7, 2, 6]

# Tuples can be convert in to lists
list3 = list(('forth', 'fifth', 'sixth')) # it returns ['forth', 'fifth', 'sixth']

# Lists can contain mixed types
['Michael', 10, 'Thriller', 0.5, True]

# Combine lists result in a sequence of then
list1 + [10, 9, 5, 7, 2, 6] # it's equal to ['first', 'second', 'third', 10, 9, 5, 7, 2, 6]

# Sublists can be get using a index interval
# from the inicial element to the last (not included)
list1[0:2] # it's equal to ['first', 'second']
list1[1:3] # it's equal to ['second', 'third']

# Get every element on a set interval
list1[::2] # it's equal to ['first', 'third']

# Get the lenght of a list
len(list1)               # it returns 3
len([10, 9, 5, 7, 2, 6]) # it returns 6

# Sort the elements of a list
sorted((5,4,7,1))                 # it returns [1, 4, 5, 7]
sorted((5,4,7,1), reverse = True) # it returns [7, 5, 4, 1]
list2.sort()                      # is change de value of list2 to [2, 5, 6, 7, 9, 10]
list2.sort(reverse = True)        # is change de value of list2 to [10, 9, 7, 6, 5, 2]

# List elements can be other lists or tuples
list4 = [1, 2, ['nesting', 'tuple'], (2.4), (5, (4, 0))]
list4[0]         # it's equal to 1
list4[2]         # it's equal to ['nesting', 'tuple']
list4[2][1][1:4] # it's equal to 'upl'
list4[4][1]      # it's equal to (4, 0)

# Lists are mutable, then their elements can be changed by index
list1[-1] = 'last' # is change de value of list1 to ['first', 'second', 'last']
list1[0:2] = [1,2] # is change de value of list1 to [1, 2, 'last']

# Add elements in the end of the list
list1 = list1 + ['...']        # is change de value of list1 to [1, 2, 'last', '...']
list1.extend(['another one'])  # is change de value of list1 to [1, 2, 'last', 'another one', '...']
list1.append(['another list']) # is change de value of list1 to [1, 2, 'last', 'another one', '...', ['another list']]

# Convert a string to a list (default delimiter is space)
"Michael Jackson's concert".split()    # it returns ['Michael', "Jackson's", 'concert']
"Michael Jackson's concert".split('a') # it returns ['Mich', 'el J', "ckson's concert"]

# Variables of list are storage as reference
list1 = ['first', 'second', 'third'] # list1 is equal to ['first', 'second', 'third']
list2 = list1                        # list1 and list2 are equal to ['first', 'second', 'third']
list1.append('forth')                # list1 and list2 are equal to ['first', 'second', 'third', 'forth']
list1 = ['new list']                 # list1 is equal to ['new list']
                                     # list2 still is equal to ['first', 'second', 'third', 'forth']

# Copy a list without using reference
list1 = ['first', 'second', 'third'] # list1 is equal to ['first', 'second', 'third']
list2 = list1[:]                     # list1 and list2 are equal to ['first', 'second', 'third']
list1 = ['new list']                 # list1 is equal to ['new list']
                                     # list2 still is equal to ['first', 'second', 'third']
