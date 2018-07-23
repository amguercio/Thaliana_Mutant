#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=40G
#SBATCH --time=2-00:15:00     # 2 days and 15 minutes
#SBATCH --output=ref_index.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="indexing"
#SBATCH -p koeniglab


##Download reference into reference-index-specific folder

##gunzip reference.fa.gz


##	##Indexing Reference for BWA Mem##	##


module load bwa/0.7.12

bwa index \
-a bwtsw /rhome/guercioa/bigdata/genomes/A_thaliana/thaliana_index.fa \
-p /rhome/guercioa/bigdata/genomes/A_thaliana



##	##Indexing reference for GATK##	##


module load picard/2.10.0

java -jar /opt/linux/centos/7.x/x86_64/pkgs/picard/2.10.0/lib/picard.jar CreateSequenceDictionary \
R= /rhome/guercioa/bigdata/genomes/A_thaliana/thaliana_index.fa \
O= /rhome/guercioa/bigdata/genomes/A_thaliana/thaliana_index.dict  


module load samtools/1.4.1


samtools faidx /rhome/guercioa/bigdata/genomes/A_thaliana/thaliana_index.fa







