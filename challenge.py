# code challenge with TL
''' Add up and print the sum of the all of the minimum elements of each inner array:[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
The expected output is given by:4 + -1 + 9 + -56 + 201 + 18 = 175
You may use whatever programming language you'd like.Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process. '''

'''outer_array variable is holding the list of all arrays'''
outer_array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
'''mins variable will store the minimum values from outer_array'''
mins = []
''' loop through outer_array to find minimum values of each array in outer_array '''
for array in outer_array:
  # pull each minimum value from each array
  ''' curr_min variable will hold the minimum value from array '''
  curr_min = min(array)
  # taking mins variable and appending the curr_min from array value
  mins.append(curr_min)
# add minimum elements together and print the sum
print(sum(mins))
