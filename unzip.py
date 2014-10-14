import zipfile

def extractFile(zfile,password):
	try:
		zfile.extractall(pwd=password)
		return password
	except:
		print '[+] failed password='+password
		return
def main():
	zFile=zipfile.ZipFile('evil.zip')
	passFile=open('dictionary.txt')
	for line in passFile.readlines():
		password=line.strip('\n')
		guess=extractFile(zFile,password)
		if guess:
			print '[+] Password='+password
			exit(0)
if __name__=='__main__':
	main()