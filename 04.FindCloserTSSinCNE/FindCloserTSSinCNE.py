#!/bin/python
import re
import sys,os

def tss_deal(tss):
    tsss = {}
    with open(tss,"r") as f:
        for line in f:
            cons = line.strip().split()
            keys = cons[0] + "_" + cons[1]
            tsss[keys] = cons[1]
    return tsss

def main(bed):
    tsss = tss_deal(tss)
    with open(bed,"r") as d:
        for line in d:
            content = line.strip().split()
            ID = content[0]
            left = content[1]
            right = content[2]
            left_min = min([[abs(int(left)-int(v)),k] for k,v in tsss.items() if ID == k.split("_")[0].strip()] )
            
            right_min = min([[abs(int(right)-int(v)),k] for k,v in tsss.items() if ID == k.split("_")[0].strip()])
            print("\t".join([content[0],left,right,left_min[1],str(left_min[0]),right_min[1],str(right_min[0])]))
if __name__ == "__main__":
    tss = "11.tss.bed"
    bed = "10.20bp.bed"
    main(bed)
