#!/bin/R

tss <- read.table("11.tss.bed",header = FALSE)
names(tss) <- c("chr","tss")
cne <- read.table("10.20bp.bed",header = FALSE)
names(cne) <- c("chr","start","end")

for (i in 1:nrow(cne)) {
  tmp <- subset(tss,chr == cne$chr[i])
  l = min(abs(tmp$tss - cne$start[i]))
  r = min(abs(tmp$tss - cne$end[i]))
  cne$tssID[i] <- cne$chr[i]
  cne$left_closest[i] <- l
  cne$right_closest[i] <- r
}

write.table(cne,file="Rresult.txt",row.names = FALSE,quote = FALSE,sep = "\t")
