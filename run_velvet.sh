#!/bin/bash

echo "This gonna run velvet"


for i in {1..50}
do
echo "kmer = " + $i
out="./out/kmer_""$i"
mkdir $out
velveth $out $i -shortPaired data/real.error.large.fasta
velvetg $out
done
