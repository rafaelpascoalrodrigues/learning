# Sets are unordered sequence of elements contained by curly brackets 
# and separated by commas
set1 = {'first', 'second', 'third', 'forth'} 
set2 = set([1, 2, 3, 4])

# Values on set are unique and duplicated values are discarted
set3 = {0, 1, 0, 2, 0, 3, 0, 4, 0, 5} # it's equal to {0, 1, 2, 3, 4, 5}

# Add value to a set
set1.add('fifth') # it's equal to {'first', 'second', 'third', 'forth', 'fifth'} 
set1.add('fifth') # it's still equal to {'first', 'second', 'third', 'forth', 'fifth'}

# Remove value to a set
set1.remove('third') # it's equal to {'first', 'second', 'forth', 'fifth'} 
set1.remove('third') # it's still equal to {'first', 'second', 'forth', 'fifth'} 

# Test if there is a value the set
'forth' in set1 # it returns True
'third' in set1 # it returns False

# Combine result in a set equal to both without the duplicated values
set1 = {'first', 'second', 'third', 'forth'} 
set3 = {'first', 'second', 'forth', 'fifth'} 
set1.union(set3)                             # it returns {'first', 'second', 'third', 'forth', 'fifth'}

# Find onçy the elements that exist in both sets
set1 & set3 # it returns {'forth', 'second', 'first'}

# Test if a subset exists in a set
set2.issubset(set3)                           # it returns False
set2.issubset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}) # it returns True
