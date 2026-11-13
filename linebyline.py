
file = open("sample.txt", "r")

lines = []

for line in file:
    lines.append(line.strip())

print("List of lines:")
print(lines)

file.close()

