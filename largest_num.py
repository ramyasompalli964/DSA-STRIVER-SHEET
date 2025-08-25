def largest(arr):
  n=len(arr)
  largest=arr[0]
  for i in range(n):
    if arr[i]>largest:
      largest=arr[i]
  return largest
  
