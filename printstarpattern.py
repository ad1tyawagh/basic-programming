# print patterns : use loop and print function.
# HINT: You need to use two nested loops
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""

row = 1

while row <= 5:

  column = 1
  while column <= 5:
    print("*", end="")
    column = column + 1
  
  print()
  row = row + 1