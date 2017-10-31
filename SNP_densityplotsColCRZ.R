##SNPs across Chr plots--scaling to max for all chr (equal scaling) 
##Looking at Col, CRZ, Shared Col and CRZ


setwd("/Users/amiriamguercio/thaliana_JGCRZ/R_Analyses/SNPpos_files")


##First need to bin reads (don't want to plot every single position)
 
Binning_SNPs <- function(Chrpos_file, Chrlen) {
  bin_ChrName <<- cut(Chrpos_file$Pos, breaks = c(seq(from = 0, to =Chrlen, by= 100000)))
  table_ChrName <<- table(bin_ChrName)
  #return(bin_ChrName)
  #return(table_ChrName)
}

##Then we need to Make Axes (don't want to plot every axis bin value) 
Making_Axes <- function(Chrlen, Binnum) {
  axispos <<- as.vector(c(seq(from = 0, to =Binnum, by= (Binnum/8))))
  axislab <<- as.vector(c(seq(from = 0, to =Chrlen, by= (Chrlen/8))))
}

##Then Plot All 3 tables as SNP density plots

SNP_densityplot <- function(table1, table2, table3, ymax, poslist, lablist, Title) {
  plot <- old.par <- par(mfrow=c(1, 3))
  plot(table1, xaxt='n', xlab= "", ylab = "Number of SNPs", ylim=c(0, ymax), col= "Red", type="h")
  axis(1, at=poslist, labels=F)
  text(poslist, labels=lablist, par("usr")[1] -100, srt=20, pos = 1, xpd=T)  #-100 moves down
  plot(table2, xaxt='n', xlab = "Chromosome Position", ylab= "", ylim=c(0, ymax), col= "Blue", type="h")
  axis(1, at=poslist, labels=F)
  text(poslist, labels=lablist, par("usr")[1] -100, srt=20, pos = 1, xpd=T) 
  plot(table3, xaxt='n', xlab= "", ylab= "", ylim=c(0, ymax), col= "purple", type="h")
  axis(1, at=poslist, labels=F)
  text(poslist, labels=lablist, par("usr")[1] -100, srt=20, pos = 1, xpd=T) 
  mtext(Title, side = 4, line = 0)
}



##  ##For Chromosome 1##  ##
#For Col 
#Load file as variable
Col_Chr1 <- read.delim("JGCol_Chr1pos.txt")
#Use Binning function
Binning_SNPs(Col_Chr1, 30427671)    ##3042761 is the chr len
#We have to rename the bin + table to our desired ChrName so each is unique
bin_ColChr1 <- bin_ChrName
table_ColChr1 <- table_ChrName
#bin_ColChr1
#table_ColChr1

#For CRZ 
#Load file as variable
CRZ_Chr1 <- read.delim("JGCRZ_Chr1pos.txt")
#Use Binning function
Binning_SNPs(CRZ_Chr1, 30427671)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_CRZChr1 <- bin_ChrName
table_CRZChr1 <- table_ChrName
#bin_CRZChr1
#table_CRZChr1

#For Mutual
#Load file as variable
Both_Chr1 <- read.delim("CRZColShared_Chr1pos.txt")
#Use Binning function
Binning_SNPs(Both_Chr1, 30427671)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_BothChr1 <- bin_ChrName
table_BothChr1 <- table_ChrName
#bin_BothChr1
#table_BothChr1

##For making axes for Chr1: Bin=304
Making_Axes(30427671, 304)
axesposChr1 <- round(axispos)
axeslabChr1 <- round(axislab)

##For plotting Chr1 all 3
SNP_densityplot(table_ColChr1, table_CRZChr1, table_BothChr1, 2000, axesposChr1, axeslabChr1, "Chromosome 1")


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

#For CRZ 
#Load file as variable
CRZ_Chr2 <- read.delim("JGCRZ_Chr2pos.txt")
#Use Binning function
Binning_SNPs(CRZ_Chr2, 19698289)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_CRZChr2 <- bin_ChrName
table_CRZChr2 <- table_ChrName
#bin_CRZChr2
#table_CRZChr2

#For Mutual
#Load file as variable
Both_Chr2 <- read.delim("CRZColShared_Chr2pos.txt")
#Use Binning function
Binning_SNPs(Both_Chr2, 19698289)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_BothChr2 <- bin_ChrName
table_BothChr2 <- table_ChrName
#bin_BothChr2
#table_BothChr2

##For making axes for Chr2: Bin=196
Making_Axes(19698289, 196)
axesposChr2 <- round(axispos)
axeslabChr2 <- round(axislab)

##For plotting Chr2 all 3
SNP_densityplot(table_ColChr2, table_CRZChr2, table_BothChr2, 2000, axesposChr2, axeslabChr2, "Chromosome 2")



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

#For CRZ 
#Load file as variable
CRZ_Chr3 <- read.delim("JGCRZ_Chr3pos.txt")
#Use Binning function
Binning_SNPs(CRZ_Chr3, 23459830)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_CRZChr3 <- bin_ChrName
table_CRZChr3 <- table_ChrName
#bin_CRZChr3
#table_CRZChr3

#For Mutual
#Load file as variable
Both_Chr3 <- read.delim("CRZColShared_Chr3pos.txt")
#Use Binning function
Binning_SNPs(Both_Chr3, 23459830)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_BothChr3 <- bin_ChrName
table_BothChr3 <- table_ChrName
#bin_BothChr3
#table_BothChr3

##For making axes for Chr3: Bin=234
Making_Axes(23459830, 234)
axesposChr3 <- round(axispos)
axeslabChr3 <- round(axislab)

##For plotting Chr3 all 3
SNP_densityplot(table_ColChr3, table_CRZChr3, table_BothChr3, 2000, axesposChr3, axeslabChr3, "Chromosome 3")



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

#For CRZ 
#Load file as variable
CRZ_Chr4 <- read.delim("JGCRZ_Chr4pos.txt")
#Use Binning function
Binning_SNPs(CRZ_Chr4, 18585056)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_CRZChr4 <- bin_ChrName
table_CRZChr4 <- table_ChrName
#bin_CRZChr4
#table_CRZChr4

#For Mutual
#Load file as variable
Both_Chr4 <- read.delim("CRZColShared_Chr4pos.txt")
#Use Binning function
Binning_SNPs(Both_Chr4, 18585056)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_BothChr4 <- bin_ChrName
table_BothChr4 <- table_ChrName
#bin_BothChr4
#table_BothChr4

##For making axes for Chr4: Bin=185
Making_Axes(18585056, 185)
axesposChr4 <- round(axispos)
axeslabChr4 <- round(axislab)

##For plotting Chr4 all 4
SNP_densityplot(table_ColChr4, table_CRZChr4, table_BothChr4, 2000, axesposChr4, axeslabChr4, "Chromosome 4")




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

#For CRZ 
#Load file as variable
CRZ_Chr5 <- read.delim("JGCRZ_Chr5pos.txt")
#Use Binning function
Binning_SNPs(CRZ_Chr5, 26975502)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_CRZChr5 <- bin_ChrName
table_CRZChr5 <- table_ChrName
#bin_CRZChr5
#table_CRZChr5

#For Mutual
#Load file as variable
Both_Chr5 <- read.delim("CRZColShared_Chr5pos.txt")
#Use Binning function
Binning_SNPs(Both_Chr5, 26975502)
#We have to rename the bin + table to our desired ChrName so each is unique
bin_BothChr5 <- bin_ChrName
table_BothChr5 <- table_ChrName
#bin_BothChr5
#table_BothChr5

##For making axes for Chr5: Bin=269
Making_Axes(26975502, 269)
axesposChr5 <- round(axispos)
axeslabChr5 <- round(axislab)

##For plotting Chr5 all 5
SNP_densityplot(table_ColChr5, table_CRZChr5, table_BothChr5, 2000, axesposChr5, axeslabChr5, "Chromosome 5")





