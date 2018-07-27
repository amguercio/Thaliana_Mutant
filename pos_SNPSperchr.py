#!/usr/bin/env python

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=20G
#SBATCH --time=1-00:15:00     # 1 day and 15 minutes
#SBATCH --output=posSNPs.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="SNPpos"
#SBATCH -p koeniglab


##Annotating by Chr



##Need the filtered vcf file you plan on plotting SNPs/chrom for

import sys

Infile=open(sys.argv[1], "r")


##To separate SNPs by chromosome

        
chr1out = open("chr1SNPs.vcf", "w")
chr2out = open("chr2SNPs.vcf", "w")
chr3out = open("chr3SNPs.vcf", "w")
chr4out = open("chr4SNPs.vcf", "w")
chr5out = open("chr5SNPs.vcf", "w")

chr1pos = open("chr1pos.txt", "w")
chr2pos = open("chr2pos.txt", "w")
chr3pos = open("chr3pos.txt", "w")
chr4pos = open("chr4pos.txt", "w")
chr5pos = open("chr5pos.txt", "w")

for line in Infile:
        line = line.strip()
        parts = line.split('\t')
        CHR = parts[0]
        Pos = parts[1]
        if int(CHR) == 1:
                chr1out.write(line + "\n")
                chr1pos.write(str("1") + "\t" + Pos + "\n")
        elif int(CHR) == 2:
                chr2out.write(line + "\n")
                chr2pos.write(str("2") + "\t" + Pos + "\n")
        elif int(CHR) == 3:
                chr3out.write(line + "\n")
                chr3pos.write(str("3") + "\t" + Pos + "\n")
        elif int(CHR) == 4:
                chr4out.write(line + "\n")
                chr4pos.write(str("4") + "\t" + Pos + "\n")
        elif int(CHR) == 5:
                chr5out.write(line + "\n")
                chr5pos.write(str("5") + "\t" + Pos + "\n")
        else: 
                continue


Infile.close()
        
chr1out.close()
chr2out.close()
chr3out.close()
chr4out.close()
chr5out.close()
                
chr1pos.close()
chr2pos.close()
chr3pos.close()
chr4pos.close()
chr5pos.close()
