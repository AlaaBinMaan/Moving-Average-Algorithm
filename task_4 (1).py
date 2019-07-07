import numpy
new_list=[]
x=[9,8,7,6,5,4,3,2,1]
i=0

y=raw_input ("enter the window you want: ")
y=int(y)
z=y

size=(numpy.size(x))-(y-1)

while i < size :
    total=0.0
    j=i
    while j <(y):
        e1=x[j]
        total=total+e1
        j=j+1
    total=total/z
    new_list.append(total)
    y=y+1
    i=i+1
print(new_list)

