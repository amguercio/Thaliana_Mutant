##Creating a venn diagram


##For three-way scaled:
#install.packages('rJava')
library(rJava)
#install.packages('venneuler')
library(venneuler)

WS02 <- venneuler(c(JGCol=41619, JGCRZ=11772, WS02=702512, "JGCol&JGCRZ"=6290, "JGCol&WS02"=19653, "JGCRZ&WS02"=6459 ,"JGCol&JGCRZ&WS02"=3668))
plot(WS02, col=c("red", "blue", "yellow")) 


WS2 <- venneuler(c(JGCol=41619, JGCRZ=11772, WS2=642434, "JGCol&JGCRZ"=6290, "JGCol&WS2"=38322, "JGCRZ&WS2"=10367 ,"JGCol&JGCRZ&WS2"=5396))
plot(WS2, col=c("red", "blue", "green"))



##For three way unscaled, but with labels for each section:
# install.packages('VennDiagram')
library(VennDiagram)

grid.newpage()
draw.triple.venn(area1 = 41619, area2 = 11772, area3 = 702512, n12 = 6290, n23 = 6459, n13 = 19653, 
                 n123 = 3668, category = c("JGCol", "JGCRZ", "WS02"), lty = "blank", 
                 fill = c("red", "blue", "yellow"))

grid.newpage()
draw.triple.venn(area1 = 41619, area2 = 11772, area3 = 642434, n12 = 6290, n23 = 10376, n13 = 38322, 
                 n123 = 5396, category = c("JGCol", "JGCRZ", "WS2"), lty = "blank", 
                 fill = c("red", "blue", "green"))
