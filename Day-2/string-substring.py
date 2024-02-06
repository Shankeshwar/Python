text = "Python is awesome & great"
replace = text.replace("&", "and")
print("modified text:", replace)
substring = "is"
if substring in replace:
    print(substring, "found in the text")
else :
    print(substring,"is not found")