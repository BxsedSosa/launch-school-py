'''
11. Consider the data in the following table:

Name        | Country
------------------------
Alice       | USA
Fancois     | Canda
Inti        | Peru
Monika      | Germany
Sanyu       | Ugande
Yoshitaka   | Japan

You need to write some Python code to determin the coutnry name associated with one of the listed names. Your code should include the data structure(s) you ned and at least one test case to ensure the code works
'''

people_location = {
    'Alice':     'USA', 
    'Francois':  'Canada',
    'Inti':      'Peru',
    'Monika':    'Germany',
    'Sanyu':     'Uganda',
    'Yoshitaka': 'Japan'
}

print(people_location['Alice'])