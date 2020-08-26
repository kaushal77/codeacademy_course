def append_sum(lst):
  for i in range(3):
    print(i)
    add = lst[-1] + lst[-2]
    lst.append(add)
  return lst 

print(append_sum([1, 1, 2]))