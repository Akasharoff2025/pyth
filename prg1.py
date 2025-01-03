l1 = ['good','fine','happy','positive']
l2 = ['sad','tired','bad','frastruated','not','negetive']
str1 = input("enter your response")
flag=0
ncount=0
t=str1.split()
for i in range(len(t)):
  for j in range(len(l1)):
    if t[i]==l1[j]:
      flag=1
  for k in range(len(l2)):
    if t[i]==l2[k]:
      flag=1
      ncount=1
  if flag==0:
    print("you are failed")
  elif ncount%2==0:
      print("positive")
  else:
     print("negetive")
