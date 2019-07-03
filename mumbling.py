#!/usr/bin/env python3
'''
This time no story, no theory. The examples below show you how to write function accum:

EXAMPLES

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
'''

def accum(s):
    list1 = []
    for position,letter in enumerate(s):
        result = ""
        # print(position,letter)
        for j in range(1, position+2):
            result = result + letter
        list1.append(result.title())
    return ('-'.join(list1))
