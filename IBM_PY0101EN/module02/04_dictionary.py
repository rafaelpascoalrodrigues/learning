# Dictionaries are unordered sequence of keys that refer to elements,
# contained by curly brackets and separated by commas
dict1 = {'zero': 0, 'one': 1, 'two': 2, 'three': 3}

# Keys on dictionary are unique and duplicated entries are overwrited
dict1 = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'zero': 'ZERO'} # it's equal to {'zero': 'ZERO', 'one': 1, 'two': 2, 'three': 3}

# Get element by the key
dict1['one'] # it's equal to 1

# Test if a key exists on a dictionary
'zero' in dict1 # it's equal to True
'four' in dict1 # it's equal to False

# List all keys of a dictionary
dict1.keys()      # it results dict_keys(['zero', 'one', 'two', 'three'])
set(dict1.keys()) # it results {'zero', 'one', 'two', 'three'}

# List all values of a dictionary
dict1.values()       # it results dict_values(['ZERO', 1, 2, 3])
list(dict1.values()) # it results ['ZERO', 1, 2, 3]
