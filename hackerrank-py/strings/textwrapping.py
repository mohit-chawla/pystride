#text wrapping in python
import textwrap

input_str = raw_input()
wrap_width = int(raw_input())

wrapped_str = textwrap.wrap(input_str,wrap_width)

for i in range(len(wrapped_str)):
    print(wrapped_str[i])
