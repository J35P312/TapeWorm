import sys

def Find_cytoband(chromosome,band):
	#open the config file to retrieve the cytoband file
	with open('config', 'r') as config:
		infile=config.readline();
	configInput=infile.split("=");
	infile=configInput[1];
	infile=infile.splitlines();
	infile=infile[0];

	#open the cytoband file and search for the given band at a given chromosome
	startpos=-1;
	endpos=0;
	for line in open(infile):
		content=line.split("\t");
		#searches for the given chromosome
		if(chromosome == content[0]):
			listBand=content[3].split(".");
			if(band == listBand[0]):
				if(startpos ==-1):
					startpos=content[1];
				endpos=content[2];
			elif(band== content[3]):
				if(startpos ==-1):
					startpos=content[1];
				endpos=content[2];

	print(chromosome + "\t" + str(startpos) + "\t" + str(endpos));



#if the cytoband is given in the form chrZan, a=arm=p,q
if(len(sys.argv) == 2):
	info=sys.argv[1];
	tmpinfo=[""];
	tmpinfo[0]=info;
	info=tmpinfo;
	#tests if the cytoband is located at the p or q arm, or if the input format is invalid
	parm=info[0].split("p");
	qarm=info[0].split("q");
	if(len(info) != len(parm)):
		chromosome="chr"+parm[0];
		band="p"+parm[1];
		Find_cytoband(chromosome,band);

	elif(len(info) != len(qarm)):
		chromosome="chr"+qarm[0];
		band="q"+qarm[1];
		Find_cytoband(chromosome,band);
		
	else:
		print("invalid format, cannot find p or q");

#if the cytoband is given in the form chrZ an or Z an, a =arm=p,q
elif(len(sys.argv) ==3):
	#if the input i given at the format chrZ an, a =arm=p,q
	if(sys.argv[1][0:3] =="chr"):
		Find_cytoband(sys.argv[1],sys.argv[2]);
	else:
		Find_cytoband("chr"+sys.argv[1],sys.argv[2]);

