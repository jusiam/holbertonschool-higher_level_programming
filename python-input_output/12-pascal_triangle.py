#!/usr/bin/python3

"""
This script adds all arguments to a Python list,
and then saves them to a file.
"""

def pascal_triangle(n):
  height = int(input("Enter height of triangle: "))
  triangle = []
  row = []
  prev_row = []
  for i in xrange(0, height + 1):
    row = [j > 0 and j < i - 1 and i > 2 and prev_row[j-1] + prev_row[j] or 1 for j in xrange(0, i)]
    prev_row = row
    triangle += [row]
  return triangle[1:]

if n <= 0:
    return []
