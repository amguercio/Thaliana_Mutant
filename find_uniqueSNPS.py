#!/usr/bin/env python

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=20G
#SBATCH --time=1-00:15:00     # 1 day and 15 minutes
#SBATCH --output=uniquesnps.stdout
#SBATCH --mail-user=guercioa@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --job-name="pyvcfs"
#SBATCH -p koeniglab



##Isolating homozygous alt in desired line script

##need vcf with two lines of interest 
##sys.argv[1] = vcf filtered input file
##sys.argv[2] = column in vcf that contains wt 
##sys.argv[3] = column in vcf that contains mutant
##sys.argv[4] = outfile (should be .vcf format)

import sys


Infile=open(sys.argv[1], "r")
line1=int(sys.argv[2])
line2=int(sys.argv[3])
Outfile=open(sys.argv[4], "w")


for line in Infile:
        line = line.strip()
        if line.startswith('#'):
                continue
        else:
                parts = line.split('\t')
                ln1 = parts[line1]
                ln2 = parts[line2]
                if ln1.startswith("0/0") and ln2.startswith("1/1"): 
                        Outfile.write(line + "\n")

Infile.close()
Outfile.close()
