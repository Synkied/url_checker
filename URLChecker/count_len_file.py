import os

num_lines = sum(1 for line in open('links.txt') if line.rstrip())
print(num_lines)

os.system("pause")