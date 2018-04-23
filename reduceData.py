#!/Users/gowthamkannan/anaconda3/bin/python
import os
import sqlite3
import shutil
from shutil import copyfile
con = sqlite3.connect('Affectnet.db')
cur = con.cursor()
def reduceData():
	parent_folder='/Volumes'
	subFolder=os.listdir(parent_folder)
	for item in subFolder:
		if 'seagate' in item.lower():
			folder_name=item
	folder_name=os.path.join(parent_folder,folder_name)
	cv_data_folder=os.path.join(folder_name,'CV_PROJ_DATA')
	train_data_folder=os.path.join(folder_name,'REDUCE_DATA')
	# if os.path.exists(os.path.join(train_data_folder)) and os.path.isdir(os.path.join(train_data_folder)):
	# 	shutil.rmtree(os.path.join(train_data_folder))
	# if not os.path.exists(os.path.join(train_data_folder)):
		# os.makedirs(train_data_folder)
	sqlStatement="""select expressionID,expressionName from expressions"""
	sqlStatement="""select expressionID,expressionName from expressions"""
	cur.execute(sqlStatement)
	rows=cur.fetchall()
	expression_dict=dict()
	for item in rows:
		expression_dict[item[0]]=item[1].rstrip().strip().upper()
	expression_list=list(expression_dict.values())
	for item in expression_list:
		if not os.path.exists(os.path.join(train_data_folder,item)):
			os.makedirs(os.path.join(train_data_folder,item))
	to_folder=os.path.join(train_data_folder)
	from_folder=cv_data_folder
	categories=list(range(0, 11))
	for item in categories:
		sqlStatement='SELECT T_2.newFilePath FROM TrainDataInfo T_1 join FilePathMapping T_2 on  T_1.filePath=T_2.oldFilePath  where T_1.expressionID='+str(item)+'  ORDER BY RANDOM()  LIMIT 5000;'
		print(sqlStatement)
		cur.execute(sqlStatement)
		rows=cur.fetchall()
		copy_folder=os.path.join(to_folder,expression_dict[item])
		for eachRow in rows:
			file_name=eachRow[0].split('/')[-1]
			src=os.path.join(from_folder,eachRow[0])
			dest=os.path.join(copy_folder,file_name)
			print(src,dest)
			copyfile(src, dest)

		# print(rows[0][0].split('/')[-1])
if __name__ == '__main__':
	reduceData()
	con.close()