#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=40G
#SBATCH --time=2-00:15:00     # 2 days and 15 minutes
#SBATCH --output=my.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="dl"
#SBATCH -p koeniglab


##SNP_Calling with all lines


##	##SNP Calling with GATK##	##

module load gatk/3.7

java -jar /opt/linux/centos/7.x/x86_64/pkgs/gatk/3.7/GenomeAnalysisTK.jar \
-nt 10 \
-T UnifiedGenotyper \
-R /rhome/guercioa/bigdata/thaliana_JGCRZ/thaliana_index/thaliana_index.fa \
-I /rhome/guercioa/bigdata/thaliana_JGCRZ/realigned_bams/JGCRZ_realn.bam \
-I /rhome/guercioa/bigdata/thaliana_JGCRZ/realigned_bams/JGCol_realn.bam \
-I /rhome/guercioa/bigdata/thaliana_JGCRZ/realigned_bams/ExCol_realn.bam \
-I /rhome/guercioa/bigdata/thaliana_JGCRZ/realigned_bams/WS02_realn.bam \
-I /rhome/guercioa/bigdata/thaliana_JGCRZ/realigned_bams/WS2_realn.bam \
-o /rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/rawSNPs.vcf \
-glm BOTH	
