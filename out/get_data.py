
out = open("velvet_data.txt",'w+')
with open("collect_velvet_data.txt") as f:
	out.write("kmer\t"+"num_contigs\t"+"n50\t"+"max_length\n")
	for i,line in enumerate(f.readlines(),start=10):
		sline = line.split(' ')
		#print sline
		con = sline[3]
		n50 = sline[8][:-1]
		max_num = sline[10][:-1]
		out.write(str(i) + "\t" + con + "\t" + n50 + "\t" + max_num + "\n" )


