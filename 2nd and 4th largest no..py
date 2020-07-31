print("Enter the numbers")
l=[int(i)for i in input().split()]
if len(l)<2:
    print("minimum 2 elements are required")
else:
  l.sort()
  if len(l)>=4:
      print("2rd largest is:{0} and 4th largest is:{1}".format(l[-2], l[-4]))
  else:
      print("2rd largest is:", l[-2], " \nlength less than 4,can't find 4th largest")





