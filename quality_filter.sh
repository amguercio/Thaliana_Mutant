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



##Row 5 of vcf's = quality



##Qualityfilter Function

def qualfilter(Infile_vcf, QUAL, Outfile_vcf):

	Infile=open(Infile_vcf, "r")
	Outfile=open(Outfile_vcf, "w")


	for line in Infile:
		line = line.strip()
        if line.startswith('#'):
                continue
        else:
                parts = line.split('\t')
                SNPqual = parts[5]
                if float(SNPqual) > float(QUAL):
                        Outfile.write(line + "\n")
                else:
                        continue

	Infile.close()
	Outfile.close()


##Now run on raw SNPs file 

##For QUAL=100
qualfilter("/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs.vcf", 100, "/rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs_Qual100.vcf")





