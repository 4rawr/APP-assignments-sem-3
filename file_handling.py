file_name = "six-seven.txt"
f = open(file_name, "w")
f.write("Six.\n")
f.write("Seven.\n")
f.close()
print("The twinks are Amogus.\n")

f = open(file_name, "r")
data = f.read()
f.close()
print("Brainrot in 2020:\n")
print(data)

f = open(file_name, "a")
f.write("Jestermaxxing is the last resort 💔\n")
f.close()
print("No Huzz?\n")

f = open(file_name, "r")
data = f.read()
f.close()
print("Brainrot in 2026:\n")
print(data)

# OUTPUT:

"""
The twinks are Amogus.

Brainrot in 2020:
Six.
Seven.

No Huzz?

Brainrot in 2026:
Six.
Seven.
Jestermaxxing is the last resort 💔
"""
