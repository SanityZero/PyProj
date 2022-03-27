for line in open('list.txt'):
    list2 = []
    if len(line)==6:
        list2.append(line)
outfile = open('list2.txt', 'w')
for out_line in list2:
    outfile.write(out_line)
outfile.close()