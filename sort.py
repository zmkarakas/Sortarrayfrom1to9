def sorted_number_array(array):
  
  counter = {}
  
  for num in array:
    if num in counter:
      counter[num] += 1
      
    else:
      counter[num] = 1
      
    pointer = 0
    
    for i in range(1,10):
      while i in counter and counter[1] > 0:
        array[pointer] = i
        pointer += 1
        counter[i] -= 1
        
    return array
