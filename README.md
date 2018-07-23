# Thaliana_Mutant
Analyzing thaliana data for mutant site identification



**Indexing_Reference.sh** 
* Includes all scripts for indexing A.thaliana reference to `.amb, .ann, .bwt, .pac, .sa, .dict, .fai` file types
    * Uses `bwa/0.7.12` `picard/2.10.0` and `samtools/1.4.1`
    * These are necessary for both `bwa` and `GATK` downstream analyses
 
 
**trimmaster.sh**
* Take raw reads-> trimmed reads
    * Uses `trimmomatic/0.33` 


**alnmaster.sh**
* Take trimmed reads-> aligns, removes duplicates, and realigns around indels
    * Uses `bwa/0.7.12` `samtools/1.4.1` `picard/2.10.0` and `GATK/3.7`


**SNPcaller.sh**
* A script calling SNPs on lines from alnmaster.sh script into one vcf file
    * Uses `GATK/3.7`


**quality_filter.sh** 
* A script taking only SNP calls above a certain quality
    * Uses `python2`


**SNPs_byline.sh**
* A script separating unique and shared SNPs into new files
    * Uses `python2`


**SNPs_bychrom.sh** 
* A script separating SNPs by chromosome for each line
    * Uses `python2`
    * It also generates files for pos-only information which is useful for downstream SNP position density plots

**NumSNPs_perchrom.R** 
* A script plotting number of SNPs per chromosome for each line
    * Uses `R`
    
**SNP_densityplotsColCRZ.R** 
* A script plotting the density of SNPs in bins per chromosome for Col, CRZ, and Col CRZ shared
   * Uses `R`
   
**SNP_densityplotsColWS022.R** 
* A script plotting the density of SNPs in bins per chromosome for Col, WS02, and WS2
   * Uses `R`
   
**SNP_densityplotsColWSShared.R** 
* A script plotting the density of SNPs in bins per chromosome for Col, Col WS02 shared, and Col WS2 shared
   * Uses `R`

**Venn_diagrams.R**
* A script plotting both unscaled and scaled triple venn diagrams
   * Uses `R` with `venneuler` and `VennDiagram` packages

**snpEff.sh**
* A script annotating all variants of a given vcf file
   * Uses `snpEff/4.3r`
    
