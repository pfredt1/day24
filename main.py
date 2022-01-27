file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()

# may be a better way.  file related cde is indented
with open("my_file.txt", mode="a") as file:
    # contents = file.read()
    # print(contents)
    file.write("new text \n")