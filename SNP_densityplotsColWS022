##SNPs across Chr plots--scaling to max for all chr (equal scaling) 
##Looking at Col, WS02, Shared Col and WS2


setwd("/Users/amiriamguercio/thaliana_JGCRZ/R_Analyses/SNPpos_files")


##First need to bin reads (don't want to plot every single position)

Binning_SNPs <- function(Chrpos_file, Chrlen) {
  bin_ChrName <<- cut(Chrpos_file$Pos, breaks = c(seq(from = 0, to =Chrlen, by= 100000)))
  table_ChrName <<- table(bin_ChrName)
  #return(bin_ChrName)
  #return(table_ChrName)
}

##Make Axes 
Making_Axes <- function(Chrlen, Binnum) {
  axispos <<- as.vector(c(seq(from = 0, to =Binnum, by= (Binnum/8))))
  axislab <<- as.vector(c(seq(from = 0, to =Chrlen, by= (Chrlen/8))))
}


##Then Plot All 3 tables as SNP density

SNP_densityplot <- function(table1, table2, table3, ymax, poslist, lablist, Title) {
  plot <- old.par <- par(mfrow=c(1, 3))
  plot(table1, xaxt='n', xlab= "", ylab = "Number of SNPs", ylim=c(0, ymax), col= "Red", type="h")
  axis(1, at=poslist, labels=F)
  text(poslist, labels=lablist, par("usr")[1] -100, srt=20, pos = 1, xpd=T)  #-100 moves down
  plot(table2, xaxt='n', xlab = "Chromosome Position", ylab= "", ylim=c(0, ymax), col= "Yellow", type="h")
  axis(1, at=poslist, labels=F)
  text(poslist, labels=lablist, par("usr")[1] -100, srt=20, pos = 1, xpd=T) 
  plot(table3, xaxt='n', xlab= "", ylab= "", ylim=c(0, ymax), col= "Green", type="h")
  axis(1, at=poslist, labels=F)
  text(poslist, labels=lablist, par("usr")[1] -100, srt=20, pos = 1, xpd=T) 
  mtext(Title, side = 4, line = 0)
}


##  ##For Chromosome 1##  ##
#For Col 
#Load file as variable
Col_Chr1 <- read.delim("JGCol_Chr1pos.txt")
#Use Binning function
Binning_SNPs(Col_Chr1, 30427671)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_ColChr1 <- bin_ChrName
table_ColChr1 <- table_ChrName
#bin_ColChr1
#table_ColChr1

#For WS02 
#Load file as variable
WS02_Chr1 <- read.delim("WS02_Chr1pos.txt")
#Use Binning function
Binning_SNPs(WS02_Chr1, 30427671)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS02Chr1 <- bin_ChrName
table_WS02Chr1 <- table_ChrName
#bin_WS02Chr1
#table_WS02Chr1

#For WS2
#Load file as variable
WS2_Chr1 <- read.delim("WS2_Chr1pos.txt")
#Use Binning function
Binning_SNPs(WS2_Chr1, 30427671)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS2Chr1 <- bin_ChrName
table_WS2Chr1 <- table_ChrName
#bin_WS2Chr1
#table_WS2Chr1

##For making axes for Chr1: Bin=304
Making_Axes(30427671, 304)
axesposChr1 <- round(axispos)
axeslabChr1 <- round(axislab)

##For plotting Chr1 all 3
SNP_densityplot(table_ColChr1, table_WS02Chr1, table_WS2Chr1, 2000, axesposChr1, axeslabChr1, "Chromosome 1")




##  ##For Chromosome 2##  ##
#For Col 
#Load file as variable
Col_Chr2 <- read.delim("JGCol_Chr2pos.txt")
#Use Binning function
Binning_SNPs(Col_Chr2, 19698289)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_ColChr2 <- bin_ChrName
table_ColChr2 <- table_ChrName
#bin_ColChr2
#table_ColChr2

#For WS02 
#Load file as variable
WS02_Chr2 <- read.delim("WS02_Chr2pos.txt")
#Use Binning function
Binning_SNPs(WS02_Chr2, 19698289)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS02Chr2 <- bin_ChrName
table_WS02Chr2 <- table_ChrName
#bin_WS02Chr2
#table_WS02Chr2

#For WS2
#Load file as variable
WS2_Chr2 <- read.delim("WS2_Chr2pos.txt")
#Use Binning function
Binning_SNPs(WS2_Chr2, 19698289)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS2Chr2 <- bin_ChrName
table_WS2Chr2 <- table_ChrName
#bin_WS2Chr2
#table_WS2Chr2

##For making axes for Chr2: Bin=196
Making_Axes(19698289, 196)
axesposChr2 <- round(axispos)
axeslabChr2 <- round(axislab)

##For plotting Chr2 all 3
SNP_densityplot(table_ColChr2, table_WS02Chr2, table_WS2Chr2, 2000, axesposChr2, axeslabChr2, "Chromosome 2")




##  ##For Chromosome 3##  ##
#For Col 
#Load file as variable
Col_Chr3 <- read.delim("JGCol_Chr3pos.txt")
#Use Binning function
Binning_SNPs(Col_Chr3, 23459830)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_ColChr3 <- bin_ChrName
table_ColChr3 <- table_ChrName
#bin_ColChr3
#table_ColChr3

#For WS02 
#Load file as variable
WS02_Chr3 <- read.delim("WS02_Chr3pos.txt")
#Use Binning function
Binning_SNPs(WS02_Chr3, 23459830)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS02Chr3 <- bin_ChrName
table_WS02Chr3 <- table_ChrName
#bin_WS02Chr3
#table_WS02Chr3

#For WS2
#Load file as variable
WS2_Chr3 <- read.delim("WS2_Chr3pos.txt")
#Use Binning function
Binning_SNPs(WS2_Chr3, 23459830)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS2Chr3 <- bin_ChrName
table_WS2Chr3 <- table_ChrName
#bin_WS2Chr3
#table_WS2Chr3

##For making axes for Chr3: Bin=234
Making_Axes(23459830, 234)
axesposChr3 <- round(axispos)
axeslabChr3 <- round(axislab)

##For plotting Chr3 all 3
SNP_densityplot(table_ColChr3, table_WS02Chr3, table_WS2Chr3, 2000, axesposChr3, axeslabChr3, "Chromosome 3")




##  ##For Chromosome 4##  ##
#For Col 
#Load file as variable
Col_Chr4 <- read.delim("JGCol_Chr4pos.txt")
#Use Binning function
Binning_SNPs(Col_Chr4, 18585056)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_ColChr4 <- bin_ChrName
table_ColChr4 <- table_ChrName
#bin_ColChr4
#table_ColChr4

#For WS02 
#Load file as variable
WS02_Chr4 <- read.delim("WS02_Chr4pos.txt")
#Use Binning function
Binning_SNPs(WS02_Chr4, 18585056)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS02Chr4 <- bin_ChrName
table_WS02Chr4 <- table_ChrName
#bin_WS02Chr4
#table_WS02Chr4

#For WS2
#Load file as variable
WS2_Chr4 <- read.delim("WS2_Chr4pos.txt")
#Use Binning function
Binning_SNPs(WS2_Chr4, 18585056)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS2Chr4 <- bin_ChrName
table_WS2Chr4 <- table_ChrName
#bin_WS2Chr4
#table_WS2Chr4

##For making axes for Chr4: Bin=185
Making_Axes(18585056, 185)
axesposChr4 <- round(axispos)
axeslabChr4 <- round(axislab)

##For plotting Chr4 all 4
SNP_densityplot(table_ColChr4, table_WS02Chr4, table_WS2Chr4, 2000, axesposChr4, axeslabChr4, "Chromosome 4")



##  ##For Chromosome 5##  ##
#For Col 
#Load file as variable
Col_Chr5 <- read.delim("JGCol_Chr5pos.txt")
#Use Binning function
Binning_SNPs(Col_Chr5, 26975502)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_ColChr5 <- bin_ChrName
table_ColChr5 <- table_ChrName
#bin_ColChr5
#table_ColChr5

#For WS02 
#Load file as variable
WS02_Chr5 <- read.delim("WS02_Chr5pos.txt")
#Use Binning function
Binning_SNPs(WS02_Chr5, 26975502)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS02Chr5 <- bin_ChrName
table_WS02Chr5 <- table_ChrName
#bin_WS02Chr5
#table_WS02Chr5

#For WS2
#Load file as variable
WS2_Chr5 <- read.delim("WS2_Chr5pos.txt")
#Use Binning function
Binning_SNPs(WS2_Chr5, 26975502)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_WS2Chr5 <- bin_ChrName
table_WS2Chr5 <- table_ChrName
#bin_WS2Chr5
#table_WS2Chr5

##For making axes for Chr5: Bin=269
Making_Axes(26975502, 269)
axesposChr5 <- round(axispos)
axeslabChr5 <- round(axislab)

##For plotting Chr5 all 5
SNP_densityplot(table_ColChr5, table_WS02Chr5, table_WS2Chr5, 2000, axesposChr5, axeslabChr5, "Chromosome 5")






