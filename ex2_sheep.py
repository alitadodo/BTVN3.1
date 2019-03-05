# #2.1
greeting =("Hello, my name is Dat and these are my ship sizes: ")
size_sheep = [5, 7, 300, 90, 24, 50, 75]
print(greeting)
print(size_sheep)

# #2.2
n = max(size_sheep)
print("now my biggest sheep has size ", (n), "let sear it")

# #2.3
max_index = size_sheep.index(n)
size_sheep[max_index] = 8
print("After shearing, here is my flock\n", size_sheep)

#2.4
m = 0
while m < len(size_sheep):
    size_sheep[m] = size_sheep[m] + 50
    m += 1
print("one mounth has passed , now here is my flock\n", size_sheep)


#2.5
greeting =("Hello, my name is Dat and these are my ship sizes: ")
size_sheep = [5, 7, 300, 90, 24, 50, 75]
print(greeting)
print(size_sheep)

n = max(size_sheep)
print("now my biggest sheep has size ", (n), "let sear it")

max_index = size_sheep.index(n)
size_sheep[max_index] = 8
print("After shearing, here is my flock\n", size_sheep)

print("MONTH 1")
m = 0
while m < len(size_sheep):
    size_sheep[m] = size_sheep[m] + 50
    m += 1
print("one mounth has passed , now here is my flock\n", size_sheep)

n = max(size_sheep)
print("now my biggest sheep has size ", (n), "let sear it")

max_index = size_sheep.index(n)
size_sheep[max_index] = 8
print("After shearing, here is my flock\n", size_sheep)

print("MONTH 2")
m = 0
while m < len(size_sheep):
    size_sheep[m] = size_sheep[m] + 50
    m += 1
print("one mounth has passed , now here is my flock\n", size_sheep)

n = max(size_sheep)
print("now my biggest sheep has size ", (n), "let sear it")

max_index = size_sheep.index(n)
size_sheep[max_index] = 8
print("After shearing, here is my flock\n", size_sheep)


print("MONTH 3")

m = 0
while m < len(size_sheep):
    size_sheep[m] = size_sheep[m] + 50
    m += 1
print("one mounth has passed , now here is my flock\n", size_sheep)

tong = sum(size_sheep)
print("My flock has size in total:",tong)
print("I would get ", tong, "* 2$ =", tong * 2,"$")

