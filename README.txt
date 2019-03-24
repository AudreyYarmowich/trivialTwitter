i.   Benjamin Yarmowich -- TheBestStudent@gatech.edu

ii.  CS 3251 Networking: Febrauary 12th 2019 Programming Assignment 1

iii. ttweetsrv.py 		#the server as requested in the documents
     ttweetcli.py 		#the client as requested in the documents
     ttweet_protocol.txt 	#the protocol for ttweet as written
     sample.png			#a screenshot of the Test Scenario executed on the shuttles (server was running on shuttle 4 and the client was running on shuttle 1)
     README.txt 		#the document that explains the homework submision

iv. The code for ttweetsrv and ttweetcli are written exclusively in Python 3.4.5 (it should work in all versions of Python 3 but I have extensively tested it in 3.4.5)
    If Python3.4.5 is not present on your machine I will provide temporary install instructions for a unix machine below

	If python 3.4.5 is installed but is not currently being pointed to double check the .bashrc file and then run "source ~/.bashrc"

	To run the ttweet program on the shuttles:
		In Bash use ifconfig to find the ip address of the shuttle that will be your host
		Run "python ttweetsrv.py <host address> <port number>"
		Open another tab/window of bash
		Run "python ttweetcli.py -d/u <host address> <port number> "Message"" \
			For full usage documentation run "python ttweetcli.py -usage" 

	To run the ttweet program on a local machine:
		In cmd or bash run "python ttweetsrv.py" this will default the host to 127.0.0.1 and port to 13069
		Open another tab/window of cmd or bash
		Run "python ttweetcli.py -d/u <host address> <port number> "Message"" \
			For full usage documentation run "python ttweetcli.py -usage" 
			If you provide no arguements ttweetcli.py will upload a default message to 127.0.0.1:13069

v. For an output sample after running the provided Test Scenario please see sample.png

vi. See ttweet_protocol.txt for the full protocol description

vii. Known Bug: While running the server on the shuttles if a connection is attempted while the server is still processing the last request, the server will report error 98 and will respond to the newest request when it can.
		In this case the server prints "Server Socket Error: [Errno 98] Address already in use" and waits for the address to be available before returning its response


How to install Python 3.4.5 on a cc.shuttle:
	Open an ssh connection to the shuttle
	"mkdir ~/python"
	"cd ~/python"
	"wget https://www.python.org/ftp/python/3.4.5/Python-3.4.5.tgz"
	"tar zxfv Python-3.4.5.tgz"
	"cd Python-3.4.5/"
	"./configure --prefix=$HOME/python"
	"make"
	"make install"
	"vim ~/.bashrc"
	scroll to the bottom of the file
	"i"
	"export PATH=$HOME/python/Python-3.4.5/:$PATH"
	":wq"
	"source ~/.bashrc"
	
	now running python --version should return Python 3.4.5

To uninstall:
	"rm -r ~/python"
	"vim ~/.bashrc"
	scroll to the line reading "export PATH=$HOME/python/Python-3.4.5/:$PATH"
	"dd"
	":wq"
	