# Exercise 1

### 1.1 Suppose you have a sorted list of 128 names, and you’re searching through it using binary search. What’s the maximum number of steps it would take?

log 128 base 2 = 7

There will be a maximum of 7 steps

### 1.2 Suppose you double the size of the list. What’s the maximum number of steps now?

There will be a maximum of 8 steps. Doubling 128 results in 256

log 256 base 2 = 8
There will be a max of 8 steps.

In conclusion, doubling tne size of list, increases the max number of steps by 1

## Give the run time for each of these scenarios in terms of big O.

### 1.3 You have a name, and you want to find the person’s phone number in the phone book.

O(log n) - Phonebook is sorted alphabetically by name, so binary seaarch can be used

### 1.4 You have a phone number, and you want to find the person’s name in the phone book. (Hint: You’ll have to search through the whole book!)

O(n) - The phonenumber is never sorted, so one has to go through every single entry from top to bottom. Linear search

### 1.5 You want to read the numbers of every person in the phone book.

O(n) - The number of operations (reading) grows as the number of persons in the phone book increases

### 1.6 You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer—you may be surprised!)

O(n) - Even when we might thiknk we are only reading the fraction of the phone book . If "As" make up 1/26th of the book, you are doing 1/26⋅n operations.
