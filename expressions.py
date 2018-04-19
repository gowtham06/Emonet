#!/Users/gowthamkannan/anaconda3/bin/python
import csv, sqlite3

con = sqlite3.connect("Affectnet.db")
cur = con.cursor()
def insertExpressions():
	cur.execute("""DROP TABLE if exists expressions""");
	cur.commit()
	cur.execute("CREATE TABLE IF NOT EXISTS expressions (expressionID int, expressionName text);") # use your column names here
	file_name='/Users/gowthamkannan/Desktop/expression.csv'
	with open(file_name,'r') as fin: # `with` statement available in 2.5+
	    # csv.DictReader uses first line in file for column headings by default
	    # dr = csv.DictReader(fin) # comma is default delimiter
	    # for i in dr:
	    # 	print(i)
	    # to_db = [(i['ExpressionID'], i['Expression']) for i in dr]
	    for line in fin:
	    	expressionID=int(line.split(',')[0])
	    	expressionName="""'"""+line.split(',')[1]+"""'"""
	    	sqlStatemet="INSERT INTO expressions (expressionID, expressionName) VALUES (%d, %s)" %(expressionID,expressionName)
	    	print(sqlStatemet)
	    	cur.execute(sqlStatemet)
	    	con.commit()

	# cur.executemany("INSERT INTO expressions (expressionID, expressionName) VALUES (?, ?);", to_db)
	# con.commit()
	con.close()
def insertTrainingData():
	cur.execute("DROP TABLE if EXISTS TrainDataInfo")
	cur.execute("CREATE TABLE IF NOT EXISTS TrainDataInfo (filePath text,faceX int,faceY int,faceWidth int,faceHeight int,expressionID int );") # use your column names here
	cur.execute("""CREATE INDEX file_path_index ON TrainDataInfo (filePath)""")
	# file_name='/Users/gowthamkannan/Desktop/expression.csv'
	file_name='/Users/gowthamkannan/Desktop/training.csv'
	with open(file_name,'r') as fileRead:
		for lineNos,line in enumerate(fileRead):
			if(lineNos!=0):
				lineSplit=line.split(',')
				filePath="""'"""+lineSplit[0]+"""'"""
				try:
					faceX=int(lineSplit[1])
					faceY=int(lineSplit[2])
					faceWidth=int(lineSplit[3])
					faceHeight=int(lineSplit[4])
					expressionID=int(lineSplit[6])
				except:
					faceX=-1
					faceY=-1
					faceWidth=-1
					faceHeight=-1

				sqlStatemet="INSERT INTO TrainDataInfo (filePath,faceX,faceY,faceWidth,faceHeight,expressionID) VALUES (%s, %d,%d,%d,%d,%d)" %(filePath,faceX,faceY,faceWidth,faceHeight,expressionID)
				print(lineNos,sqlStatemet)
				cur.execute(sqlStatemet)
	con.commit()
	cur.close()			

if __name__ == '__main__':
	# insertExpressions()
	insertTrainingData()


