##Stacks(linear structure)
  A stack is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end.
This end is commonly referred to as the"top"
The end opposite the top is the "base"

#Stack ordering:LIFO:Last in First Out
#Newer items are near the top while older items are near the base

#Push: for insertion
#Pop : for removing item from the stack
#Peek: return the item from the top of the stack without removing it

#Two types of memory:
#Stack memory
-limited in size
-fast access
A special region of the memory(in the RAM)
local variables
##A call stack:
It is an abstract data type that stores information about the active subroutines,methods,functions of a computer program
#Stack heap
no size limits
-low access because of pointers
it is not managed automatically
-reference types and objects are on the heap(Java)
-use of garbage collector
unless memory leak:dead object in the memory