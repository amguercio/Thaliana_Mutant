##Making bar graphs for Per-Chromosome SNP data to Compare Samples

setwd("/Users/amiriamguercio/thaliana_JGCRZ/Analyses")


##First let's just graph the # of SNPs/ sample/ chromosome
SNP_perchrom<-read.table("SNP_perchromdata.txt", sep= "\t", header=TRUE)

#SNP_perchrom
#is a datatable like this:
#Chr  Col CRZ
#1  Chr1  1157  7
#2  Chr2  200 89
#3  Chr3  12 145
#4  Chr4  16   10
#5  Chr5  5200 801


##Now let's make a variable for the 'height' or number of SNPs 
height <- rbind(SNP_perchrom$Col, SNP_perchrom$CRZ)  #You do this step to graph both on the same barplot

#height
#is a vector like this
#[,1] [,2] [,3] [,4] [,5]
#[1,] 1157  200 12  16  5200
#[2,] 7 89  145 10  801



##Now let's define a function to make a barplot of number of SNPs per chromosome for the two lines
#The inpute when calling the function are your original table as Infile
#height is the vector we created above using rbind
#Line1 is the first line you inluded in height and Line2 is the second, these will be used to label the legend for each line
#besideTorF just allows you to change whether the two lines are plotted as neighboring barplots or stacked barplots--give T or F here

SNPchrom_Barplot <- function(Infile, height, Line1, Line2, besideTorF) {
  plot <- barplot(height, names.arg=Infile$Chr,
                  main = "SNPs Per Chromosome for Each Sample",
                  beside=besideTorF,
                  xlab = "Chromosome Number",
                  ylab= "Number of SNPs",
                  col = c("Pink", "Light Blue")
  )
  
  legend("topleft",
         c(Line1, Line2),
         fill = c("Pink", "Light Blue")
  )
  return(plot)
}

##Now let's call the function and plot a stacked barplot for our data
SNPchrom_Barplot(SNP_perchrom, height, "Col", "CRZ", F)

##How about a barplot with the lines side by side
SNPchrom_Barplot(SNP_perchrom, height, "Col", "CRZ", T)




