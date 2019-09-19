#This is a exercise to review:
print("Exercise 1.")
name = input("introduce your name:")
count = 0
lettersonname = name.split()
for i in lettersonname:
    count = count + 1
name = name.upper()
print(name, " have ", count, " letters.")