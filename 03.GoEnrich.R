
library(tidyverse)
setwd("./03_GoEnrich/go_anno.csv")
dta <- read.table("go_anno.csv",header = TRUE,sep = ",")
dta %>% 
  group_by(Description) %>% 
  mutate(n=n()) %>% 
  select("Description","Ontology","n") %>% 
  slice(1) %>% 
  arrange(Ontology,-n) -> aa

# select the top 15 pathway ordered the genes number in every Ontology
aa %>% group_by(Ontology) %>% slice(1:15) -> aa

aa$Ontology <- factor(aa$Ontology,levels = c("biological_process","cellular_component","molecular_function"),
                      labels = c("BP","CC","MF"))

aa$type[aa$Ontology == "BP"] <- 1
aa$type[aa$Ontology == "CC"] <- 2
aa$type[aa$Ontology == "MF"] <- 3

aa %>% 
  ggplot(aes(x=reorder(Description,type),y = n,fill = Ontology)) + geom_bar(stat = "identity") + coord_flip() + 
  labs(x="Description",y="gene number")
ggsave(filename = "./03_GoEnrich/shipx.tiff",height = 10,width = 9,dpi = 300)
