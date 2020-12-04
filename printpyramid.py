# print patterns : use loop and print function.
# HINT: You need to use two nested loops
"""
* 
* * 
* * * 
* * * * 
* * * * *
"""

row = 1

while row <= 5:

  # to print a row
  current = 1
  # to print a column in a row
  while current <= 5:
    print("*", end=" ")
    current = current + 1
  
  print() # for new line
  row = row + 1