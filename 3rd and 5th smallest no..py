print("Enter the numbers")
l=[int(i)for i in input().split()]
if len(l)<3:
    print("minimum 3 elements are required")
else:
  l.sort()
  if len(l)>=5:
      print("3rd smallest is:{0} and 5th smallest is:{1}".format(l[2], l[4]))
  else:
      print("3rd largest is:", l[2], " \nlength less than 5,can't find 5th smallest")




