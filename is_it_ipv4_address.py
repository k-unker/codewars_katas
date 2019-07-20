#!/usr/bin/env python3
'''
Implement String#ipv4_address?, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading 0s, spaces etc.
'''
def ipv4_address(address):
    a = address.split('.')
    if len(a) != 4:
        return False
    for x in a:
        try:
            if not x.isdigit():
                return False
            if int(x) < 0 or int(x) > 255:
                return False
            if str(int(x)) != x:
                return False
        except:
            return False
    return True
