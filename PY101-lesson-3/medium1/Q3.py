"""
Q3. Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buufer becomes full, any new elements will displace the oldest elements in the buffer

She wrote two implementation of the code for adding elements to the buffer
"""


def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


"""
Is there a difference between these imiplementations, other than the way she is adding an element to the buffer?
"""

"""
The first method mutates the given 

The second method adds to the buffer by concatenating with the plus operator 
without mutating the original buffer
"""
