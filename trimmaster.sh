#!/bin/bash -l

#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=40G
#SBATCH --time=2-00:15:00     # 2 days and 15 minutes
#SBATCH --output=trimming.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="trimming"
#SBATCH -p koeniglab



## Need:
##paired end read files (with path) as $1 and $2
NAME=$(basename "$1" | cut -d_ -f1)

#basename takes away path and file extension
#then pipe into cut to take away everything after the _ delimiter; but only of the first line of the file


##	##Trimmomatic Script##  ##

module load trimmomatic/0.33

java -jar /opt/linux/centos/7.x/x86_64/pkgs/trimmomatic/0.33/bin/trimmomatic.jar PE -phred33 \
$1 \
$2 \
"$NAME"_forward_paired.fq.gz \
"$NAME"_forward_unpaired.fq.gz \
"$NAME"_reverse_paired.fq.gz \
"$NAME"_reverse_unpaired.fq.gz \
ILLUMINACLIP:/opt/linux/centos/7.x/x86_64/pkgs/trimmomatic/0.33/adapters\
/TruSeq3-SE.fa:2:30:10 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:75

