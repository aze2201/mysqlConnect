#!/usr/bin/python3.6
import mysql.connector as mysql
import configparser
import sys, getopt
import os

exitScript=False

config = configparser.ConfigParser()
config.sections()


# read input argument
try:
	opts, args = getopt.getopt(sys.argv[1:],"h:c:",["","config="])
	if len(opts)==0:
		sys.exit(2)
except getopt.GetoptError:
	print ('mainscriptMySQL.py -c <config file>')
	sys.exit(2)


for opt, arg in opts:
	if opt == '-h':
		print ('test.py -c <inputfile>')
		sys.exit()
	elif opt in ("-c", "--config"):
		inputfile = arg
		config.read(arg)

connection  = config['DEFAULT']['connection']
user        = config['DEFAULT']['user']
schemaName  = config['DEFAULT']['schemaName']
password    = config['DEFAULT']['password']
output    = config['DEFAULT']['output']
dport    = config['DEFAULT']['dbport']

sqlStringFile = config['DEFAULT']['sqlfile']

db = mysql.connect(
	host = connection,
	port = dport,
	user = user,
	passwd = password,
	database = schemaName
)



# empty and tune output file
def writeFile(data,filename):
	os.system('> '+filename)
	tmp=open(filename,'w+')
	for i in data:
		tmp.write(str(i).replace(')','').replace('(',''))
		tmp.write('\n')
	tmp.close()

cursor = db.cursor()

sqlString = open(sqlStringFile).read()
cursor.execute(sqlString)
result = cursor.fetchall()
writeFile(result,output)



