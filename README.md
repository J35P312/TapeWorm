TapeWorm is a software that returns the basepair position of a cytoband. The cytoband and the chromosome is given as a command line argument when starting TapeWorm:
python TapeWorm 1q32.3
python TapeWorm chr1 q32.3
python TapeWorm 1 q32.3

will return the position of 1q32.3:
chr1	211300000	21440000

the original cytoband data was retrieved from:
http://hgdownload.cse.ucsc.edu/goldenPath/hg38/database/
This file contains the cytobands of the human genome.

to change the cytobandfile open the config file and change the file from:
inputfile=cytoBandhg38.txt
into
inputfile=new_cytoband_file

