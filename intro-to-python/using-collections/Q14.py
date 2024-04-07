'''
14. Assume you have the following sequences:

Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence. Print the final result so you can see all the values.
'''

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tup = (None, True, False)
my_range = range(10, 60, 10)

zip_iterables = zip(my_str, my_list, my_tup, my_range)
print(list(zip_iterables))
