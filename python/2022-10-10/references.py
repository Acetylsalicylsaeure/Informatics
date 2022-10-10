# reference refers to a specific location in the memory (a value)
a=1
b=a
# a directly references 1, b indirectly references 1 by referencing a
a+=1
# a now references 2, old reference is deleted
# garbage collection: removal of values in memory that no longer have a live
# reference
# python does this automatically

# some complex data types provide .close(), .drop() functions, eg tables. use
# these to manually free up memory when no longer needed
