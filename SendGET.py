#!/usr/bin/python
import requests
import sys, getopt

def action(inputfile,outputfile):
	with open(inputfile,"rt") as file:
		output_file = open("responses.txt","at")
		for x in file:
			try:
				get_response = requests.get(x)
				print(x + "" + str(get_response))
			except:
				print("No Response For :" + x)
				output = "No Response For :" + x
				output_file.write(output)
				continue		
		output = x +"  " + str(get_response)
		output_file.write(output)
	file.close()
	output_file.close()	
	print("------All output written to "+ outputfile +"-------")

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'SendGET.py -i <inputifle> -o <outputfile>'
		print 'SendGET.py -h for detailed help' 
		sys.exit(2)
	for opt,arg in opts:
		if opt == '-h':
			print 'SendGET.py -i <inputfile> -o <outputfile> \n https:// or http:// protocol must be specifies in input file \n ipnut file data format: \n http://*.***.**/ \n https://www.****.*** \n http://***.*****.com/ \n  . . . . . . . . . . .\n '
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile= arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	action(inputfile,outputfile)
		

if __name__ == "__main__":
   main(sys.argv[1:])