#!/usr/bin/env python3
'''
Task:
This kata requires you to write an object that receives a file path and does operations on it. NOTE FOR PYTHON USERS: You cannot use modules os.path, glob, and re
The purpose of this kata is to use string parsing, so you're not supposed to import external libraries. I could only enforce this in python.
Testing:
Python:

>>> master = FileMaster('/Users/person1/Pictures/house.png')
>>> master.extension()
'png'
>>> master.filename()
'house'
>>> master.dirpath()
'/Users/person1/Pictures/'
'''
class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
    def extension(self):
        self = self.filepath.split('.')[1]
        return self
    def filename(self):
        fullpath = ('.').join(self.filepath.split('.')[:-1])
        self = fullpath.split('/')[-1]
        return self
    def dirpath(self):
        dirpath = ('/').join(self.filepath.split('/')[:-1])
        self = dirpath + '/'
        return self
