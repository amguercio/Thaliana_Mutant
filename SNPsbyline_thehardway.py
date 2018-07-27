#!/usr/bin/env python

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=20G
#SBATCH --time=1-00:15:00     # 1 day and 15 minutes
#SBATCH --output=my.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="dl"
#SBATCH -p koeniglab



##Isolating homozygous alt in desired line script

def homalt_finder(Infile_vcf, columnof_line, Outfile_vcf):

	Infile=open(Infile_vcf, "r")
	Outfile=open(Outfile_vcf, "w")
	lineinfo=int(columnof_line)


	for line in Infile:
		line = line.strip()
        if line.startswith('#'):
                continue
        else:
                parts = line.split('\t')
                refalt = parts[lineinfo]
                if refalt.startswith("1/1"):
                        Outfile.write(line + "\n")
                else: 
                        continue

	Infile.close()
	Outfile.close()


##Now run on Qual filtered rawsnps file for each desired line

##For JGCRZ, column = 10
homalt_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 10, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_SNPs.vcf")

##For JGCol, column = 11
homalt_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 11, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCol_SNPs.vcf")

##For ExCol, column = 9
homalt_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 9, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ExCol_SNPs.vcf")

##For WS02, column = 12
homalt_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 12, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS02_SNPs.vcf")

##For WS2, column = 13
homalt_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 13, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS2_SNPs.vcf")




##Isolating shared homozygous calls between two lines

def sharedhomSNP_finder(Infile_vcf, columnof_shared1, columnof_shared2, Outfile_vcf):

        Infile=open(Infile_vcf, "r")
        Outfile=open(Outfile_vcf, "w")
        shared1=int(columnof_shared1)
        shared2=int(columnof_shared2)


        for line in Infile:
                line = line.strip()
                if line.startswith('#'):
                        continue
                else:
                        parts = line.split('\t')
                        sh1 = parts[shared1]
                        sh2 = parts[shared2]
                        if sh1.startswith("1/1") and sh2.startswith("1/1"):
                                Outfile.write(line + "\n")
                        else: 
                                continue

        Infile.close()
        Outfile.close()



##For JGCol and JGCRZ shared, JGCol = 11, JGCRZ = 10
sharedhomSNP_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 11, 10, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/CRZColShared_SNPs.vcf")

##For JGCol and WS02 shared, JGCol = 11, WS02 = 12
sharedhomSNP_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 11, 12, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS02Shared_SNPs.vcf")

##For JGCol and WS02 shared, JGCol = 11, WS2 = 13
sharedhomSNP_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 11, 13, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS2Shared_SNPs.vcf")

##For JGCRZ and WS02 shared, JGCRZ = 10, WS02 = 12
sharedhomSNP_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 10, 12, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/CRZWS02Shared_SNPs.vcf")

##For JGCRZ and WS2 shared, JGCRZ = 10, WS02 =  13
sharedhomSNP_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf", 10, 13, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/CRZWS2Shared_SNPs.vcf")










