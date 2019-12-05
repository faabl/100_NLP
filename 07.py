# -*- coding: utf-8 -*-
from string import Template

# def xyz_string(x,y,z):

#     return '{}時の{}は{}'.format(x,y,z)

def xyz_string(x,y,z):
    s = Template('$hour時の$targetは$value')
    return s.substitute(hour= x,target = y, value = z)

x = 12
y = '気温'
z = 22.4
print(xyz_string(x,y,z))