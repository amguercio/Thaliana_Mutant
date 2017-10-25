# Thaliana_Mutant
Analyzing thaliana data for mutant site identification


Indexing_Reference.sh includes all scripts for indexing A.thaliana reference to .amb, .ann, .bwt, .pac, .sa, .dict, .fai file types
  These are necessary for both BWA and GATK downstream analyses
  
*_pipe.sh scripts are pipes that take raw reads-> realigned bams for each line

SNP_calling.sh is a script calling SNPs on all lines from _*pipe.sh script into one vcf file

quality_filter.sh is a script taking only SNP calls above a certain quality

SNPs_byline.sh is a script separating unique and shared SNPs into new files

SNPs_bychrom.sh is a script separating SNPs by chromosome for each line
  It also generates files for pos-only information which is useful for downstream SNP position density plots
