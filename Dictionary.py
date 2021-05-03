dict = {'Adam': 12, 'Joe': 45, 'Liz': 78}
print(dict['Adam'])

dict['Adam'] = 13
print(dict['Adam'])
# dict.clear()  # remove all the entries in the dictionary
# del dict remove the dictionary itself

print(dict.items()) # return all the key value pairs
print(dict.keys())
print(dict.values())