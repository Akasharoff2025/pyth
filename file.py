f=open("file.txt","r")
lines=[line for line in f]
print(lines)
new_lines=[x.strip() for x in lines]
print(new_lines)
