# -*- coding: utf-8 -*-

file_name="hightemp.txt"
ans =0
with open(file_name) as f:
    for line in f:
        ans += 1

print(ans,"行")