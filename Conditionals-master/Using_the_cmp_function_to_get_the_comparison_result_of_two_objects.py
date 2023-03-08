# a cmp function which allows you to determine if one object is less than, equal to, or greater than
# another object. This function can be used to pick a choice out of a list based on one of those three options.
# Suppose you need to print 'greater than' if x > y, 'less than' if x < y and 'equal' if x == y
from filecmp import cmp


['equal','greater than','less than', ][cmp(x,y)]
print(cmp(x,y))