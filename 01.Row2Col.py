#!/bin/python
import openpyxl as op
def write():
    bg = op.load_workbook("tem.xlsx")
    sheet = bg["Sheet1"]
    i = 1
    with open("test.txt","r") as f:
        for line in f:
            line = line.strip().split()
            for x in range(1,len(line)+1):
                #print(str(i) + "\t" + str(x) + "\t" + line[x-1])
                sheet.cell(x,i,line[x-1])
            i += 1
        bg.save("tem.xlsx")
                
if __name__ == "__main__":
    write()
    #bg.save("tem2.xlsx")
