#!/Users/gowthamkannan/anaconda3/bin/python
import sqlite3,sys

def deleteTables():
	db = sqlite3.connect('AffectNet.db')
	cursor = db.cursor()
	cursor.execute('''DROP TABLE if exists expressions ''')
	db.commit()
	db.close()

def createTables():
	db = sqlite3.connect('AffectNet.db')
	cursor = db.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS TrainDataInfo (filePath text,faceX int,faceY int,faceWidth int,faceHeight int,expressionID int );") 
	cursor.execute("CREATE TABLE IF NOT EXISTS expressions (expressionID int, expressionName text);") 
	cursor.execute("CREATE TABLE ")
	
	



def query_table():
	db = sqlite3.connect('AffectNet.db')
	cursor = db.cursor()
	cursor.execute('''select * from expressions ''')
	rows=cursor.fetchall()
	print(rows)
	db.commit()
	db.close()
if __name__ == '__main__':
	arg=sys.argv[1]
	print(arg)
	if(arg=="delete"):
		deleteTables()
	if(arg=="query"):
		query_table()
