#Create
greeting =("Welcome to our shop, what do you want: ")
print(greeting)
store = ["T-Shirt", "Sweater"]
for index, item in enumerate(store):
    print(index+1, item,sep=".")




#Read
store = ["T-Shirt", "Sweater"]
n = (input("Enter new item: "))
store.append(n)
for index, item in enumerate(store):
    print(index+1, item,sep=".")




#Update
store = ["T-Shirt", "Sweater", "Jeans"]
for index, item in enumerate(store):
    print(index+1, item,sep=".")
n = int(input("enter number: "))
m = input("Update position: ")
store[n-1] = m
for index, item in enumerate(store):
    print(index+1, item,sep=".")




#Delete
store = ["T-Shirt", "Sweater", "Jeans"]
for index, item in enumerate(store):
    print(index+1, item,sep=".")
n = int(input("Delete position: "))
del store[n-1]
for index, item in enumerate(store):
    print(index+1, item,sep=".")


