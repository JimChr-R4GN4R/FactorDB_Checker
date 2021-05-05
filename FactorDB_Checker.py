import requests
from bs4 import BeautifulSoup


def status_check_factorDB(n):
	s = requests.get('http://factordb.com/index.php?query='+str(n))

	if s.status_code == 200:
		results = BeautifulSoup(s.text, "lxml").text
		results = results.replace('\n\nfactordb.com\n\n\nSearch\nSequences\nReport results\nFactor tables\nStatus\nDownloads\nLogin\n\n\n\n\n\n\nResult:\nstatus (?)\ndigits\nnumber\n','').replace('\n\n','').split('\n')

		if "C" == results[0]:
			print("Status: Composite, no factors known\n")
		elif "CF" == results[0]:
			print("Status: Composite, factors known\n" + results[2])
		elif "FF" == results[0]:
			print("Status: Composite, fully factored\nFactors: " + results[2])
		elif "P" == results[0]:
			print("Status: Definitely prime\n")
		elif "Prp" == results[0]:
			print("Status: Probably prime\n")
		elif "U" == results[0]:
			print("Status: Unknown\n")
		elif "Unit" == results[0]:
			print("Status: Just for '1'\n")
		elif "N" == results[0]:
			print("Status: This number is not in database (and was not added due to your setting\ns)\n")
		elif "*" == results[0]:
			print("Status: Added  to database during this request\n")
	else:
		print("Status code:",str(s.status_code))

while 1:

	n = input("Number: ")

	if n == "":
		break
	else:
		try:
			n = int(n)
			status_check_factorDB(n)
		except ValueError:
			print("[!] Please give an integer")
