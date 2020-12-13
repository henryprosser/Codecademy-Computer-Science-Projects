def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))

  first = 0
  last = len(data) - 1

 # Iterative loop to find the search value
  while first <= last:
    mid = (first + last) // 2

    # Check if the middle is empty
    if not data[mid]:
      left = mid - 1
      right = mid + 1

      while True:
        if left < first and right > last:
          print("{0} is not in the dataset".format(search_val))
          return

        elif right <= last and data[right]:
          mid = right
          break

        elif left >= first and data[left]:
          mid = left
          break

        right += 1
        left -= 1

    # Check if the search value is equal to the middle
    if data[mid] == search_val:
      print("{0} found at position {1}").format(search_val, mid)
      return

    # Check if search value is less than the middle
    elif search_val < data[mid]:
      last = mid - 1

    # Check if search value is greater than the middle
    elif search_val > data[mid]:
      first = mid + 1

  print("{0} is not in the dataset".format(search_val))


    
          
    
  