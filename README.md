# Thaliana_Mutant
Analyzing thaliana data for mutant site identification



**Indexing_Reference.sh** 
* Includes all scripts for indexing A.thaliana reference to `.amb, .ann, .bwt, .pac, .sa, .dict, .fai` file types
    * Uses `bwa` `picard` and `samtools`
    * These are necessary for both `bwa` and `GATK` downstream analyses
 
 
**_pipe.sh**
* Pipe scripts that take raw reads-> realigned bams for each line
    * Uses `trimmomatic` `bwa` `samtools` `picard` and `GATK`


**SNP_calling.sh**
* A script calling SNPs on all lines from _*pipe.sh script into one vcf file
    * Uses `GATK`


**quality_filter.sh** 
* A script taking only SNP calls above a certain quality
    * Uses `python`


**SNPs_byline.sh**
* A script separating unique and shared SNPs into new files
    * Uses `python`


**SNPs_bychrom.sh** 
* A script separating SNPs by chromosome for each line
    * Uses `python`
    * It also generates files for pos-only information which is useful for downstream SNP position density plots
