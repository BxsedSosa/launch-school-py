'''
3. Without runnin the following code, what does it print? why?
'''

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

'''
The program will print out:

Product2
Product not found

since the second time the function is ran the arugment given are integers and the match/case is needing strings for the case to be true.
'''