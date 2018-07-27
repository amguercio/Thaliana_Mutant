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


##Annotating by Chr

##To separate SNPs by chromosome

def chrom_finder(Infile_vcf, Chrom_num, Outfile_vcf):

	Infile=open(Infile_vcf, "r")
	Outfile=open(Outfile_vcf, "w")
	

	for line in Infile:
        line = line.strip()
        parts = line.split('\t')
        CHR = parts[0]
        	if CHR.startswith("Pt") or CHR.startswith("Mt"):
        		continue
        	elif int(CHR) == int(Chrom_num):
        		Outfile.write(line + "\n")
        	else:
        		continue

	Infile.close()
	Outfile.close()


##For JGCRZ
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_SNPs.vcf", 1, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr1.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_SNPs.vcf", 2, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr2.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_SNPs.vcf", 3, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr3.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_SNPs.vcf", 4, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr4.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_SNPs.vcf", 5, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr5.vcf")

##For JGCol
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCol_SNPs.vcf", 1, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr1.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCol_SNPs.vcf", 2, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr2.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCol_SNPs.vcf", 3, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr3.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCol_SNPs.vcf", 4, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr4.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCol_SNPs.vcf", 5, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr5.vcf")

##For JGCRZJGCol Shared
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/CRZColShared_SNPs.vcf", 1, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr1.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/CRZColShared_SNPs.vcf", 2, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr2.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/CRZColShared_SNPs.vcf", 3, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr3.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/CRZColShared_SNPs.vcf", 4, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr4.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/CRZColShared_SNPs.vcf", 5, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr5.vcf")


##For WS02
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS02_SNPs.vcf", 1, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr1.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS02_SNPs.vcf", 2, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr2.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS02_SNPs.vcf", 3, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr3.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS02_SNPs.vcf", 4, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr4.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS02_SNPs.vcf", 5, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr5.vcf")

##For WS2
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS2_SNPs.vcf", 1, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr1.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS2_SNPs.vcf", 2, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr2.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS2_SNPs.vcf", 3, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr3.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS2_SNPs.vcf", 4, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr4.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/WS2_SNPs.vcf", 5, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr5.vcf")


##For ColWS02 Shared
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS02Shared_SNPs.vcf", 1, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr1.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS02Shared_SNPs.vcf", 2, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr2.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS02Shared_SNPs.vcf", 3, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr3.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS02Shared_SNPs.vcf", 4, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr4.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS02Shared_SNPs.vcf", 5, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr5.vcf")

##For ColWS2 Shared
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS2Shared_SNPs.vcf", 1, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr1.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS2Shared_SNPs.vcf", 2, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr2.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS2Shared_SNPs.vcf", 3, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr3.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS2Shared_SNPs.vcf", 4, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr4.vcf")
chrom_finder("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/ColWS2Shared_SNPs.vcf", 5, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr5.vcf")




##To make file of just SNP positions for downstream

def pos_maker(Infile_vcf, Outfile_vcf):

	Infile=open(Infile_vcf, "r")
	Outfile=open(Outfile_vcf, "a")
	
	Outfile.write("Pos" + "\t" + "Instances" + "\n")
	
	for line in Infile:
        line = line.strip()
        parts = line.split('\t')
        Pos = parts[1]
		Outfile.write(Pos + "\t" + str("1") + "\n")
		
	Infile.close()
	Outfile.close()
	
##For JGCRZ
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr1.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCRZ_Chr1pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr2.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCRZ_Chr2pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr3.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCRZ_Chr3pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr4.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCRZ_Chr4pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCRZ_Chr5.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCRZ_Chr5pos.txt")


##For JGCol
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr1.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCol_Chr1pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr2.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCol_Chr2pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr3.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCol_Chr3pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr4.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCol_Chr4pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/JGCol_Chr5.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/JGCol_Chr5pos.txt")


##For JGCRZJGCol Shared
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr1.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/CRZColShared_Chr1pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr2.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/CRZColShared_Chr2pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr3.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/CRZColShared_Chr3pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr4.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/CRZColShared_Chr4pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/CRZColShared_Chr5.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/CRZColShared_Chr5pos.txt")


##For WS02
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr1.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS02_Chr1pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr2.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS02_Chr2pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr3.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS02_Chr3pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr4.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS02_Chr4pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS02_Chr5.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS02_Chr5pos.txt")


##For WS02
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr1.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS2_Chr1pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr2.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS2_Chr2pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr3.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS2_Chr3pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr4.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS2_Chr4pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/WS2_Chr5.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/WS2_Chr5pos.txt")


##For ColWS02 Shared
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr1.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS02Shared_Chr1pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr2.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS02Shared_Chr2pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr3.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS02Shared_Chr3pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr4.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS02Shared_Chr4pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS02Shared_Chr5.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS02Shared_Chr5pos.txt")


##For ColWS2 Shared
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr1.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS2Shared_Chr1pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr2.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS2Shared_Chr2pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr3.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS2Shared_Chr3pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr4.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS2Shared_Chr4pos.txt")
pos_maker("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/ColWS2Shared_Chr5.vcf", "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/SNPs_bychrom/SNPs_bychrompos/ColWS2Shared_Chr5pos.txt")











