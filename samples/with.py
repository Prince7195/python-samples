with open("text/with.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\nLine 4")
    print(content)