file = open("text/read.txt", "r")
#content = file.read()
                        # Line 1
                        # Line 2
                        # Line 3
# print(content)

file.seek(0) # changing every line into an array
# content = file.readlines() # ['Line 1\n', 'Line 2\n', 'Line 3']
# content = file.readline() # Line 1
content = file.readlines()
content = [i.rstrip("\n") for i in content] # ['Line 1', 'Line 2', 'Line 3']
print(content)
file.close()