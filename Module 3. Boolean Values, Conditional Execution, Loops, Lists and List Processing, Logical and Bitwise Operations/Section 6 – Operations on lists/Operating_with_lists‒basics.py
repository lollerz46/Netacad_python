"""
Imagine a list โ not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.

Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.

Note: assume that the source list is hard-coded inside the code โ you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

Hint: we encourage you to create a new list as a temporary work area โ you don't need to update the list in situ.
"""

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
temp = []

for i in range(len(my_list)):
    print(my_list[i])
    if my_list[i] not in temp:
        temp.append(my_list[i])
        print("questo รจ temp", temp)
    
print("The list with unique elements only:")
print(my_list)
print(temp)

### SOLUTION ###

"""
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for number in my_list:  # Browse all numbers from the source list.
	if number not in new_list:  # If the number doesn't appear within the new list...
		new_list.append(number)  # ...append it here.
my_list = new_list[:]  # Make a copy of new_list.
print("The list with unique elements only:")
print(my_list)
"""
