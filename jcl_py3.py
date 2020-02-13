import njelib_py3
import sys
from importlib import reload

class TSO:

	def JCL(self, ohost='', rhost='', host='', filename='', username='', password=''):

		reload(njelib_py3)
		self.ohost = ohost
		self.rhost = rhost
		self.host = host
		self.filename = filename
		self.username = username
		self.password = password
		#self.session = session



		print("[+] OHOST:", self.ohost)
		print("[+] RHOST:", self.rhost)
		print("[+] IP   :", self.host)
		print("[+] File :", self.filename)
		print("[+] User :", self.username)

		nje = njelib_py3.NJE(self.ohost, self.rhost)
#		nje.set_debuglevel(0)
		t = nje.session(self.host, port=175, timeout=5, password=self.password)
		if not t:
			print("[!] Could not connect")
			sys.exit(1)

		print("[+] Connected")
		print("===================")
		print("[+] Sending file:", self.filename)
		with open(self.filename, "r") as myfile:
			data = myfile.readlines()
		print("---------10--------20--------30---------40---------50---------60---------70---------80\n")
		for l in data:
			print(l.strip("\n"))
		print("\n---------10--------20--------30---------40---------50---------60---------70---------80")
		nje.sendJCL(self.filename, self.username)
		print("===================")
		print("[+] Response Received")
		if len(nje.getNMR()) > 0:
			print("[+] NMR Records")

		print("===================")
		for record in nje.getNMR():
			if 'NMRUSER' in record:
				print("[+] User Message")
				print("[+] To User:", record['NMRUSER'])
				print("[+] Message:", record['NMRMSG'])

		print("===================")
		print("[+] Records in SYSOUT:")
		result = []
		for record in nje.getSYSOUT():
			if 'Record' in record and record['Record'] != b' ':
				result.append(record['Record'])
		return(result)