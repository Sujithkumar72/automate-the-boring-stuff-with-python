name = input("Enter your name: ")
#plain variable  - single line comment
print("Hello, " + name)

'''
print format
print using fstring
as well the multi-line comment
'''
print("Hello, {} using format method".format(name),)
print(f'Hello, {name} using fstring and separators', end="\t")
print("...Nothing Ends...")
