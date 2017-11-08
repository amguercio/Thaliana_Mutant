##You must locally download snpEff because of problems trying to save databases to the origin file on the cluster 
##You can also download on your home computer but there are often issues with java compatibility on osx

##To download and unzip snpEff:
##On biocluster in my home directory
#wget http://sourceforge.net/projects/snpeff/files/snpEff_latest_core.zip
#unzip snpEff_latest_core.zip



##java -jar snpEff.jar databases
##This will output thousands of organisms' databases, get ready.
##Here are the ones I'm interested in 

#Hordeum_vulgare  Hordeum_vulgare  ENSEMBL_BFMPP_32_162  http://downloads.sourceforge.net/project/snpeff/databases/v4_3/snpEff_v4_3_ENSEMBL_BFMPP_32_162.zip
#Arabidopsis_lyrata   Arabidopsis_lyrata  ENSEMBL_BFMPP_32_24  http://downloads.sourceforge.net/project/snpeff/databases/v4_3/snpEff_v4_3_ENSEMBL_BFMPP_32_24.zip
#Arabidopsis_thaliana  Arabidopsis_thaliana  ENSEMBL_BFMPP_32_24 http://downloads.sourceforge.net/project/snpeff/databases/v4_3/snpEff_v4_3_ENSEMBL_BFMPP_32_24.zip

##Now to download the A.thaliana database I'm using for analyzing these SNPs
java -jar /rhome/guercioa/bigdata/SNPEFF/snpEff/snpEff.jar download -v Arabidopsis_thaliana

##Now to annotate your vcf file (I was looking at an only-JGCRZ vcf file)
#java -Xmx4g -jar path/to/snpEff/snpEff.jar -v -stats path/to/stats/file.html referencename path/to/vcf/file.vcf > path/to/outvcf/file.ann.vcf

java -Xmx4g -jar /rhome/guercioa/bigdata/SNPEFF/snpEff/snpEff.jar -v -stats /rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_annotations/stats.html Arabidopsis_thaliana /rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_annotations/JGCRZ_forsift.recode.vcf > /rhome/guercioa/bigdata/thaliana_JGCRZ/SNPcalls_vcfs/JGCRZ_annotations/JGCRZ_snpeffannotated.vcf


