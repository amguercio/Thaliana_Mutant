#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=40G
#SBATCH --time=2-00:15:00     # 2 days and 15 minutes
#SBATCH --output=snpping.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="SNPping"
#SBATCH -p koeniglab


##	##SNP Calling with GATK##	##


## Need:
##realigned (no dup) .bam files (with path) as $1 and $2



module load gatk/3.7

java -jar /opt/linux/centos/7.x/x86_64/pkgs/gatk/3.7/GenomeAnalysisTK.jar \
-nt 10 \
-T UnifiedGenotyper \
-R /rhome/guercioa/bigdata/genomes/A_thaliana/thaliana_index.fa \
-I $1 \
-I $2 \
-o rawSNPs.vcf \
-glm BOTH	

#both calls both SNPs and indels

