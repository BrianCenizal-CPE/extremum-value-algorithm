def find_extremum(number):
  if not number: #if list is empty
    print("Error: The list is empty!")
    return None, None
    
  valid_list = []
  
  for i in range(1, len(number)+1): # create a new list of only valid numbers
    result = number[i-1]
    if not isinstance(result, (int)):
        print(f"Error: {result} is not an integer.")
    else:
        valid_list.append(result)
  
  if not valid_list: #if the new list is empty
    print("Error: No valid integers in the list!")
    return None, None
    
  max_value = min_value = valid_list[0]#assign both as the first value of the list, making sure its an int ofcourse
  
  for i in range(1, len(valid_list)):
    if valid_list[i] > max_value:
      max_value = valid_list[i]
    if valid_list[i] < min_value:
      min_value = valid_list[i]

  return max_value, min_value


print("Extremum Value Algorithm")
print("=========================\n")

#normal values with some invalid values
data = ["bb",1,5,14,1,545,135,13,6,2]
maximum, minimum = find_extremum(data)
print("List: ", data)
print("Maximum value found: ",  maximum)
print("Minimum value found: ", minimum)

#trying out negative values
data2 = [-10, -5, 0, 25, -3]
maximum, minimum = find_extremum(data2)
print("\nList2:", data2)
print("Maximum:", maximum)
print("Minimum:", minimum)

#trying out invalid values
data3 = ["-10", -5.54542, "0", "hello", 'asf']
maximum, minimum = find_extremum(data3)
print("\nList3:", data3)
print("Maximum:", maximum)
print("Minimum:", minimum)
