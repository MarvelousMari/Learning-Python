import re

# Your code goes here
find_members = []
for function in dir(re):
    if "find" in function:
        find_members.append(function)

print(sorted(find_members))
