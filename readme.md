### 对不同列数的行进行转置
将test.txt中的每一行转置成对应的一列
```shell
python Row2Col.py
```
### 文件匹配
- kog_1为每个KOG富集条目所包含的基因
- kog_matches.m8中第二列为基因
***要求***：将kog_1中每个KOG条目在kog_matches.m8中所包含的基因找出来
```shell
python 02.shipx.py > 20220512_results.txt
```
### Go analysis 画图
```
Rscript 03.GoEnrich.R
```

### FindCloserTSSinCNE
- 11.tss.bed TSS位点文件
- 10.20bp.bed CNE文件
- 找出CNE区域左右两侧离得最近的TSS位点（同一条染色体上）
```python
python FindCloserTSSinCNE.py > results.txt
``` 
 


