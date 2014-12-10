tuples = []

for i in xrange(10, 90):
    with open("output-{}-stats.tab".format(i)) as f:
        f.readline()
        line = f.readline().strip().split('\t')
        tuples.append((str(i), line[0], line[5], line[8]))

with open("ABYSS_OUTPUT_FILE.txt", 'w') as f:
    for tup in tuples:
        f.write("\t".join(tup) + "\n")
