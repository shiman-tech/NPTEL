#string immutable,but can be sliced and concaenated


s='hello'
s+='world'
s1=s+'puppy'
print(s)

#list mutable

l=[1,2,4]
l2=l 

#both l and l2 points to the same list, so any changes made to either list affects both

#concatenation and slicing creates a new list so above statement is false for this case

l3=l
l3=l3+[5,6]
l4=l
l4=l4[1:]
print(l)
print(l3)
print(l4)

#but l3+=[5,6] moddifes in place so they would still point to the same list object
#+= implies are modifiying the same list/string so it takes in-place 
