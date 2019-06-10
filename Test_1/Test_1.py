import os

file = open('test.txt', 'r')
code_blocks = []
file1 = None

for line in file:

    line = line.lower()
    line = line.strip()
    print("> " + line)

    # keep writing data into the file until you reach the next tag
    if line.startswith("//cpc_tag:"):
        # when you reach a new tag then close the current file tag, and open a new one
        if file1 is not None:
            file1.close()
        file1 = open(line[10:] + '.txt', 'w')

        # adding a record to the list of blocks
        code_blocks.append(line[10:])

    else:
        if (file1 is not None) and line:
            file1.write(line + '\n')

file1 = open('blocks.py', 'w')
file1.write("code_blocks = [")

lim = len(code_blocks)
ctr = 0

for ele in code_blocks:
    if ctr < lim - 1:
        file1.write("'" + ele + "'" + ',')
    else:
        file1.write("'" + ele + "'" + ']')
    ctr += 1
file1.close()
