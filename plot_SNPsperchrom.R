#!/usr/bin/env Rscript


##to run files in my directory that end with *.txt through my R script to generate SNPs/chrom graphs

###!/bin/bash
###FILES=*.txt
##for f in $FILES
##do
##  Rscript script.R $f
###done


setwd("/rhome/guercioa/bigdata/thaliana_JGCRZ/BSA/vcf_processing")


##The argument given from the command line is the infile name
args = commandArgs(trailingOnly=TRUE)
Infile<-args[1]


snps <- read.delim(Infile)
snps <- data.frame(snps)

library(ggplot2)

SNPdensity <- ggplot(snps, aes(x=pos)) + geom_histogram(binwidth = 1e5) + ylim(0,500)

Outfile<-unlist(strsplit(Infile, split=".", fixed=TRUE))[1]
##take just the first part of the Infile name

Outfile<-paste0(Outfile,".pdf")
##add a .pdf to the infile name

pdf(Outfile)
print(SNPdensity)
dev.off()
##print it out!
