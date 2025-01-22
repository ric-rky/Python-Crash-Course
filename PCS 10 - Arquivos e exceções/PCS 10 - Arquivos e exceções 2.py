# 10.1
from pathlib import Path

path = Path("C:\\Users\\ricar\\OneDrive\\Documentos\\Python Study Files\\learning_python.txt")

my_text = path.read_text()
#print(my_text)

my_text_lines = my_text.splitlines()

lines = ''
for line in my_text_lines:
    lines += line

print(lines)

# 10.2
my_text_C = my_text.replace('Python', 'C')
print(my_text_C)




