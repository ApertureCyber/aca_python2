"""
Building on the prior example from 1_set_demo.py, this demonstration uses arg parse to give commandline control
to the script

Example: Read an input of hash values, remove the duplicates and print the results to stdout and / or save to file

Solution: Let's give the option to the user to either print to screen and or save results to a file
"""

import argparse

# code from 1_set_demo.py
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

# create a parser and add arguments
parser = argparse.ArgumentParser(description='Test program')
# Add a single argument that, if invoked, set the variable to true (action='store_true')
parser.add_argument('-s', '--save', dest='save_results', action='store_true', help='Need to add in help message')
args = parser.parse_args()

#code from 1_set_demo.py
hash_list_unique = set(hash_list_original)
print('Return Type: {}; Total Hashes: {}; Total Unique: {}'.format(type(hash_list_unique),
                                                                   len(hash_list_original),
                                                                   len(hash_list_unique)))

# Iterate through the 'set' to access the values individually
for line in hash_list_unique:
    print(line)

# Save results to file
if args.save_results:
    # open a file in current directory and write the results to the files
    with open('results.txt', 'w') as f:
        # f.write doesn't support writing type: set to a file. The set result needs to be converted to type string
        f.write('\n'.join(hash_list_unique))



