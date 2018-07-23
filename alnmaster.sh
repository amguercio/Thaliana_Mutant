#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=40G
#SBATCH --time=2-00:15:00     # 2 days and 15 minutes
#SBATCH --output=map_n_rm_n_realn.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="map_n_rm_n_realn"
#SBATCH -p koeniglab



##	##Align + Sam -> Bam Script##   ##
## Need:
##Trimmed fwd and reverse files (with path) as $1 and $2
NAME = $(basename "$1" | cut -d_ -f1)

#basename takes away path and file extension
#then pipe into cut to take away everything after the _ delimiter; but only of the first line of the file




module load bwa/0.7.12
module load samtools/1.4.1


bwa mem -t 10 -R "@RG\tID:Columbia_Analyses\tSM:"$NAME"\tPL:ILLUMINA" \
/rhome/guercioa/bigdata/genomes/A_thaliana/thaliana_index \
$1 \
$2 \
| samtools sort -T /tmp \
-O bam \
-o "$NAME"_rawalns.bam




##	##Removing Duplicates with Picard Script##	##

module load picard/2.10.0


java -jar /opt/linux/centos/7.x/x86_64/pkgs/picard/2.10.0/lib/picard.jar MarkDuplicates \
INPUT= "$NAME"_rawalns.bam \
OUTPUT= "$NAME"_dupfree.bam \
METRICS_FILE= "$NAME"_dupinfo.txt \
REMOVE_DUPLICATES=true \
VALIDATION_STRINGENCY=LENIENT \
TMP_DIR= /tmp



##	##Indexing reads for GATK##	##

module load samtools/1.4.1


samtools index "$NAME"_dupfree.bam




##	##GATK Realign Around Indels Script##	##

module load gatk/3.7


##First use realigner target creator

java -jar /opt/linux/centos/7.x/x86_64/pkgs/gatk/3.7/GenomeAnalysisTK.jar \
-T RealignerTargetCreator \
-R /rhome/guercioa/bigdata/genomes/A_thaliana/thaliana_index.fa \
-I "$NAME"_dupfree.bam \
-o "$NAME"_int.intervals


##Then use this outfile to help realign with indel realigner

java -jar /opt/linux/centos/7.x/x86_64/pkgs/gatk/3.7/GenomeAnalysisTK.jar \
-T IndelRealigner \
-R /rhome/guercioa/bigdata/genomes/A_thaliana/thaliana_index.fa \
-I "$NAME"_dupfree.bam \
-targetIntervals "$NAME"_int.intervals \
-o "$NAME"_realn.bam


##Now take this/these file(s) into a SNP-caller script.
