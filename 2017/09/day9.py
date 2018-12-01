import re
garbage_lenght = 0
data = open("./puzzle.txt", 'r').readline()
data = re.sub(r'!!', r'', data)
data = re.sub(r'![^\s]', r'', data)
garbage = re.findall(r'<[^\s\>]*>', data)
for char in garbage:
    garbage_lenght += len(char)-2
data = re.sub(r'<[^\s\>]*>', r'', data)
braces = re.findall(r'[\{\}]', data)
open_braces = []
score = 0
for brace in braces:
    if brace == "{":
        open_braces.append("{")
    else:
        if open_braces:
            score += len(open_braces)
            open_braces.pop()
print("day9_1:", score)
print("day9_2:", garbage_lenght)
