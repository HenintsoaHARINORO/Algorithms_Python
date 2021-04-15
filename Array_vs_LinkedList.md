#Arrays
All your elements are stored contiguously in memory.
When you need to add some elements,f you’re out of space and need to move to a
new spot in memory every time, adding a new item will be really slow.
So you ask the computer extra slots 
-You know the address for every item in the array

Reading:O(1)
Insertion:O(n)
Deletion:O(n)
#Linked List
-Your items can be anywhere in memory.
-Each item stores the address of the next item in the list.
A bunch of random memory addresses are linked together.
-You do not know the address but you have to go to the first element and so on until the item you want to find.
Reading:O(n)
Insertion:O(1)
Deletion:O(1)