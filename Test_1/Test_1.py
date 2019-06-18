import os

file = open('test.txt', 'r')
rebuild_f = open('rebuild.c', 'w')
code_blocks = []
file1 = None
fname = ''

for line in file:
    line = line.lower()
    line = line.strip()
    if not line.startswith("//cpc tag:"):
        rebuild_f.write(line + '\n')
    else:
        break

file.seek(0, 0)

for line in file:

    line = line.lower()
    line = line.strip()

    # see the code as it is parsed, on the output screen
    #print("> " + line)

    # keep writing data into the file until you reach the next tag
    if line.startswith("//cpc tag:"):
        # when you reach a new tag then close the current file tag, and open a new one
        if file1 is not None:
            file1.close()

        fname = line[11:].replace(" ", "_")
        #print(fname+'\n')
        file1 = open(fname + '.h', 'w')
        rebuild_f.write('#include"' + fname + '.h' + '"\n')
        # adding a record to the list of blocks
        code_blocks.append(fname)

    else:
        if (file1 is not None) and line:
            file1.write(line + '\n')

file1 = open('blocks.py', 'w')
file1.write("code_blocks = [")

lim = len(code_blocks)
ctr = 0

# Writing the list of the names of files created, into a.py file for later use
for ele in code_blocks:
    if ctr < lim - 1:
        file1.write("'" + ele + "'" + ', ')
    else:
        file1.write("'" + ele + "'" + ']')
    ctr += 1

file1.close()
rebuild_f.close()
