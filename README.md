# Python-with-ARP

First make sure that you have python installed on your device and if it's not installed, follow this link right here to download the latest version of python.

	https://www.python.org/downloads/

Then, when you manage to install python, you will need to install the required modules to your machine to run the script properly.
For that you will need to run these commands to carry out the installation.

	pip3 install argparse
	pip3 install scapy
	pip3 install requests
	pip3 install re
	pip3 install uuid


Once you have finished installing these modules, simply open the command prompt and type in the network you wish to scan.

when you want to start the scnan, make sure to give give your network as a target with '-t' or '--target' and enter the IP address you wish to scan along with the subnet mask.

	python Network Scanner with ARP.py -t 192.168.1.0/24




