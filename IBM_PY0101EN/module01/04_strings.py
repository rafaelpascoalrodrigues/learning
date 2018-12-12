# Strings can be contained by single ou double quotes
name = 'Michael Jackson'
album = "Thriller"

# Characters indexes on strings start on 0
name[0] # it's equal to 'M'
name[1] # it's equal to 'i'
name[2] # it's equal to 'c'

# Negative indexes starts on -1 and run strings backward
name[-1] # it's equal to 'n'
name[-2] # it's equal to 'o'
name[-3] # it's equal to 's'JacksonJackson

# Substrings can be get using a index interval
# from the inicial character to the last (not included)Jackson
name[0:4]  # it's equal to 'Mich'
name[8:12] # it's equal to 'Jack'

# Get every character on a set interval
name[::2]   # it's equal to 'McalJcsn'
name[::3]   # it's equal to 'Mhlas'
name[0:7:2] # it's equal to 'Mcal'

# Get the lenght of a string
len(name)       # it's equal to 15
len('Thriller') # it's equal to 8

# Concatenate strings
album + ' is an album from ' + name # it's equal to 'Thriller is an album from Michael Jackson'

# Repeat strings
3 * name          # it's equal to 'Michael JacksonMichael JacksonMichael Jackson'
(album + ' ') * 3 # it's equal to 'Thriller Thriller Thriller '

# Convert string to Upper Case string
album.upper() # it returns 'THRILLER'

# Convert string to Lower Case string
name.lower() # it returns 'michael jackson'

# Replace a substring on a string by another substring
name.replace('Michael', 'Janet ') # it returns 'Janet Jackson'

# Find the index of the first occurrence of a sugstring on a string
name.find('Jac') # it returns 8
name.find('Thr') # it returns -1
