#!/bin/python

with open("kog_1","r") as f:
    tem = {}
    for line in f:
        line = line.strip()
        if line.startswith("["):
            key = line.strip()
            key1 = key.split()[0][1:-1]
            key2 = " ".join(key.split()[2:])
            keys = key2 + "_" + key1
        else:
            values = line.strip().split(":")[1]
            if keys not in tem:
                tem[keys] = [values]
            else:
                tem[keys].append(values)
    #print(tem)

with open("kog_matches.m8","r") as f:
    genes = []
    for line in f:
        gene = line.strip().split("\t")
        gene = gene[1]
        genes.append(gene)
    genes = set(genes)
    genes = list(genes)
        
count = 0
for k,v in tem.items():
    k1 = k.split("_")[0]
    k2 = k.split("_")[1]
    for v1 in v:
        v1 = v1.strip()
        if v1 in genes:
            count += 1
    print(k2 + "\t" + k1 + "\t" + str(count))
    count = 0


