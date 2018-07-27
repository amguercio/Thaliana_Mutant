#!/usr/bin/env python

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=20G
#SBATCH --time=1-00:15:00     # 1 day and 15 minutes
#SBATCH --output=qualfilter.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="qualfilter"
#SBATCH -p koeniglab


##need vcf with two lines of interest 
##sys.argv[1] = vcf filtered input file
##quality score you want to filter (if 100, keeps qual >100)
##sys.argv[3] = outfile (should be .vcf format)

import sys


Infile=open(sys.argv[1], "r")
QUAL=int(sys.argv[2])
Outfile=open(sys.argv[3], "w")

##Column 5 of vcfs = quality

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
