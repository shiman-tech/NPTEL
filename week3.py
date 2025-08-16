#use of range inside list

l=list(range(5))
print(l)

#use of else clause in loops. part of for loop-break, breaks out of both- is executed when for is terminated normally i.e it completes all its iterations

for i in l:
    print(i)
else:
    print('heh')   


#expansion/shrinking of slices  
l[4:]  =[5,6,7]
print(l)
l[1:]=[1]
print(l)

#removing 1st occurence of an element
l=[1,2,2,2,3,4]
if 2 in l:
    l.remove(2)

#removing all occurences of an element

x=2
while x in l:
    l.remove(x)

print(l)    

#binary search

def binarySearch(l,v):
    
    start=0
    end=len(l)-1

    while(start<=end):
        mid=(start+end)//2
        if(l[mid]==v):
            print('found at index',mid)
            return
        elif(v>l[mid]):
            start=mid+1
        else:
            end=mid-1
    print('not found')
    

binarySearch(l,4)  

def selectionSort(l):
    for i in range(len(l)-1):
        min=i
        for j in range(i+1,len(l)):
            if(l[j]<l[min]):
                min=j
        l[i],l[min]=l[min],l[i]   

l2=[5,3,2,8,6]
selectionSort(l2)
print(l2)

def insertionSort(l):
   
    for k in range(1,len(l)): 
        j=k-1
        v=l[k]
        while(j>=0 and l[j]>v):
            l[j+1]=l[j]
            j-=1
        l[j+1] =v

l3=[5,3,2,8,6]  
insertionSort(l3)    
print(l3)

        

    




