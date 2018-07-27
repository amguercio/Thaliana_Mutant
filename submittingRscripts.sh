#!/bin/bash



#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=20G
#SBATCH --time=1-00:15:00     # 1 day and 15 minutes
#SBATCH --output=plotsnps.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="submitplotsnps"
#SBATCH -p koeniglab


FILES=*.txt
for f in $FILES
do
        Rscript plotSNPsperchrom.R $f
done

