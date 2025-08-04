# Ordered,Mutable,Heterogeneous

empty = []

# List of strings
names = ["Isha","Ranveer","Thakur"]
names[0] = "Aditi" # updating the value at index 0
print(names[1])
print(names[-1]) # Last element
print(names[1:3]) # Slicing of list 

# List of mixed data types
mixed = ["Isha",5 ,True,3.14]
# Nested list 
matrix = [[1,2],[2,3],[5,6]] # 2*3 matrix

for name in names:
    print(name)

print()
for mix in mixed:
    print(mix)

for mat in matrix:
    for val in mat:
        print(val,end=" ")
    print()
        
fruits = ["apple","banana"]
fruits.append("Cherry") # Add cherry after banana
fruits.insert(1,"Orange") # Insert oranage at index 1
fruits.extend(["Isha","Ranveer"]) 
print(fruits)
print(f"length of list : {len(fruits)}")

fruits.remove("Cherry")
fruits.pop() # remove last element from the list
print(fruits)
fruits.clear()
print(fruits)
