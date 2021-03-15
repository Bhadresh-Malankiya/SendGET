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
			print " SendGET.py -i <inputfile> -o <outputfile> \n https:// or http:// protocol must be specifies in input file \n ipnut file data format: \n http://*.***.**/ \n https://www.****.*** \n http://***.*****.com/ \n  . . . . . . . . . . .\n "
            print "100 Continue \n is sent in some circumstances when a aclient submits a requests containing a body.\nThe response indicates that the request headers were received and that the client \n should cntinue sending the body.The server returns a second response when the requests has beeen completed. \n "
            print "200 Ok \n indicates that the request was successful and that the response body contains the \n result of the request. \n"
            print "201 Created \n is returned in response to a PUT request to idicate that the request was successfull. \n"
            print "301 Moved Permanently \n redirects the browser permanently to a different URL, which is specified in the Location \n header.The client should use the new URL in the future rather \n than the original.\n"
            print "302 Found redirects \n the browser temporarily to a different URL, whihc is specified in the Location header. \n The client should use the new URL in subsequent requests.\n "
            print "304 Not Modified \n instruct the browser to use its cached copy of the requested resource. Thee server uses \n the If-Modified-Since and If-None-Match request header to determine \n whether the client has the latest version of the resource. \n"
            print "400 Bad Request \n indicates that the clent submitted and invalid HTTP request You will probably encounter \n this when you have modified a request in certain invalid ways , such as \n by placing a space character into the URL.\n "
            print "401 Unauthorized \n indicates that the server requires HTTP authentication before the request will be granted. \n The WWW-Authenticate header ocntains details on the type(s) of \n authentication supported.\n "
            print "403 Forbidden \n indicates that no one i s allowe to access the requested resource,regardless of authentication.\n"
            print "404 Not Found \n indicates that the requested resource doest not exist.\n"
            print "405 Method Not Allowed \n indicates that the method used in the request is not supported for the specified URL. \n For exampleyou may receive this status code if you attempt to \n use PUT method where it is not allowed. \n"
            print "413 Reuest Entity Too Large \n If you are probing for buffer overflow vulnerabilities in native code, \n and therefore are submitting long strings of data this indicates that the \n body of your request is too large fo rthe server to handle. \n"
            print "414 Request URI Too Long \n is similar to the 413 response. It indicates that URI used in the request is \n too large for the server to handle. \n"
            print "500 Internal Server error \n indicates that the server encountered an error fulfilling the request.this normally \n occurs when you have submitted unexpected input caused an unhandled \n error somewhere withing the aoolication's processing. You should closely review the full ocntents od the server's \n response for any details indicating the nature of the error. \n "
            print "503 Service Unavailable \n normally indicates that , although the web server itself is functioning and can respond \n to requests, the application accessed via the server is responding. \n You should verify whether this is the result of any action you have performed.\n "
            sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile= arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	action(inputfile,outputfile)
		

if __name__ == "__main__":
   main(sys.argv[1:])