# write a function which prints the keys and values in a dictionary in the following
# format: 'key: ' key_in_dict 'value: ' value_in_dict
def printKeyValuePairs(d1):
    for k in d1:
        print 'key: {} value: {}'.format(k, d1[k])

d1 = {'hey': 'there', 0: 'blahhhh', 'key_with_list_value': [1,2,'entry']}
# printKeyValuePairs(d)

# Write a function which takes three parameters where parameter 1 is a key,
# parameter 2 is its corresponding value and parameter 3 is a dictionary to add
# them to
def addToDictionary(k, v, d2):
    d2[k] = v

d2 = {'another': 'dictionary'}
# print d
# addToDictionary('new_key', ['new_value_list', 20], d)
# print d

# Write a function which takes a list of keys and dictionary. Print out all the
# keys in the dictionary passed in which are in the list which was passed in.
def printKeysInDict(keys, d3):
    for k in keys:
        if k in d3:
            print d3[k]

d3 = {'more keys': 'more values', 1000: ['stuff', 'in', 'a', 'list'], 1500: 2000}
# printKeysInDict(['more keys', 'dont print me'], d)

# write a function which takes a list of values and a dictionary and prints all
# the keys whose values are in the list
def printKeysFromValues(values, d4):
    key_value_pairs = d4.items()
    for key, value in key_value_pairs:
        if value in values:
            print key
d4 = {'more keys': 'more values', 1000: ['stuff', 'in', 'a', 'list'], 1500: 2000}
values = ['more values', 2000, 'not in dictionary']
printKeysFromValues(values, d4)
