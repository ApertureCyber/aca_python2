"""
Demonstration on using python's built-in set function to return a unique list

Example: Multiple, possibly duplicative hash values are identified and a unique set of hash values is needed to lookup
in the sandbox.

Solution: Let's create a code to return a unique set of hash values.
"""
# The original input containing duplicative information can be from a text file, command line, API query.
# Create a list object of that data.
hash_list_original = [
    'ffce2bf37e994f61df3597096bf3a03d',
    '2161e7ee14fda3d6ca5abd3e00e1bd23',
    '2161e7ee14fda3d6ca5abd3e00e1bd23',
    '2161e7ee14fda3d6ca5abd3e00e1bd23',
    '6972dbb69e487839225da7ef881c4791',
    '6972dbb69e487839225da7ef881c4791',
    'b7b1acd12927cc95c11203c8e766b83e',
    'a653f10d62699f0e120b7936e3e76b7b',
    'b7b1acd12927cc95c11203c8e766b83e',
    'b7b1acd12927cc95c11203c8e766b83e',
    ]

# Use the set builtin to remove the duplicate values
# object returned is class type 'set'
hash_list_unique = set(hash_list_original)

# Use len() to count the items within the list
print('Return Type: {}; Total Hashes: {}; Total Unique: {}'.format(type(hash_list_unique),
                                                                   len(hash_list_original),
                                                                   len(hash_list_unique)))

# Iterate through the 'set' to access the values individually
for line in hash_list_unique:
    print(line)
