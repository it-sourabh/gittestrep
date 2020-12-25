# Tuple is a collection of Python objects much like a list. The sequence of values
# stored in a tuple can be of any type, and they are indexed by integers.
# Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary, it is more common
# to define a tuple by closing the sequence of values in parentheses. This helps in understanding the
# Python tuples more easily.
coordinates = (1, 6)
# Tuples are immutable unlike lists. Hence, they cannot be modified
print(coordinates)
# But, we can create a list of tuples
co_ods = [(4, 7), (3, 6), (9, 3)]
co_ods[2] = (3,7)
print(co_ods)

