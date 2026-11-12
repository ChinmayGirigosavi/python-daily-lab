"""
Topic: Reading and Managing Files
"""

# File Modes Reference:
# "r"  -> Read a file
# "r+" -> Read and write a file
# "a"  -> Append information at the end of a file (cannot edit existing text)
# "w"  -> Write / overwrite a file

aboutme = open("aboutme.txt", "r")

print(aboutme.readable())
print(aboutme.read())

# Reset cursor to the start of the file before reading lines again
aboutme.seek(0)

for line in aboutme.readlines():
    print(line)

# Always close the file to free up system resources
aboutme.close()