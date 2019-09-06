#!/usr/bin/env python3

'''
Mothers arranged dance party for children in school.
On that party there are only mothers and their children.
All are having great fun on dancing floor when suddenly 
all lights went out.Its dark night and no one can see 
eachother.But you were flying nearby and you can see 
in the dark and have ability to teleport people anywhere you 
want.

Legend:
-Uppercase letters stands for mothers,lowercase stand 
 for their children. I.E "A" mothers children are "aaaa".
-Function input:String contain only letters,Uppercase 
 letters are unique.

Task:
Place all people in alphabetical order where Mothers 
are followed by their children.I.E "aAbaBb" => "AaaBbb".
'''

def find_children(dancing_brigade):
    myarr = []
    dancing_brigade = sorted(dancing_brigade)
    for i in range(len(dancing_brigade)):
        if dancing_brigade[i].lower() in dancing_brigade or dancing_brigade[i].upper() in dancing_brigade:
            myarr.append(dancing_brigade[i])
            mysmall = dancing_brigade[i].lower()
            mylarge = dancing_brigade[i].upper()
            mycounter = dancing_brigade.count(mysmall) - dancing_brigade.count(mylarge)
            a = 0
            while a <= mycounter:
                myarr.append(dancing_brigade[i].lower())
                a += 1
    return ''.join(myarr)[:len(dancing_brigade)]
