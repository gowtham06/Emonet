#!/Users/gowthamkannan/anaconda3/bin/python
import os
import sqlite3
import shutil
from shutil import copyfile
con = sqlite3.connect('Affectnet.db')
cur = con.cursor()
def preprareData():
	curr_dir=os.getcwd()
	parentDirectory=os.path.join(curr_dir,'REDUCE_DATA')
	trainDirecotry=os.path.join(parentDirectory,'train')
	validationDirectory=os.path.join(parentDirectory,'validation_1')
	# list_files=os.listdir()
	
	# cat_files=[file for file in list_files if 'cat' in file.lower()]
	# dog_files=[file for file in list_files if 'dog' in file.lower()]
	categories=['ANGER','DISGUST','HAPPY','NONE','SAD','UNCERTAIN','CONTEMPT','FEAR','NEUTRAL','NO_FACE','SURPRISE']
	# for item in categories:
	# 	if os.path.exists(os.path.join(trainDirecotry,item)):
	# 		shutil.rmtree(os.path.join(trainDirecotry,item))
	# 	if os.path.exists(os.path.join(validationDirectory,item)):
	# 		shutil.rmtree(os.path.join(validationDirectory,item))
		
	for item in categories:
		# if not os.path.exists(os.path.join(trainDirecotry,item)):
		# 	os.makedirs(os.path.join(trainDirecotry,item))
		# if not os.path.exists(os.path.join(validationDirectory,item)):
		# 	os.makedirs(os.path.join(validationDirectory,item))
		if not os.path.exists(os.path.join(trainDirecotry,item)):
			os.makedirs(os.path.join(trainDirecotry,item))
				
	# parent_folder='/Volumes'
	# subFolder=os.listdir(parent_folder)
	# for item in subFolder:
	# 	if 'seagate' in item.lower():
	# 		folder_name=item
	# folder_name=os.path.join(parent_folder,folder_name)
	# DATA_FOLDER='VALIDATION_DATA'
	# folder_name=os.path.join(folder_name,DATA_FOLDER)
	# # print(os.listdir(folder_name))
	# sqlStatement="""select expressionID,expressionName from expressions"""
	# cur.execute(sqlStatement)
	# rows=cur.fetchall()
	# expression_dict=dict()
	# for item in rows:
	# 	expression_dict[item[0]]=item[1].rstrip().strip().upper()
	# file_counter=1
	# check_folder=['Manually_Annotated_Images']
	# for item in check_folder:
	# 	# subFolders=os.listdir(os.path.join(folder_name,item))
	# 	parentDirectory=os.path.join(folder_name,item)
	# 	subFolders=[o for o in os.listdir(parentDirectory) if os.path.isdir(os.path.join(parentDirectory,o))]
	# 	for eachSubFolder in subFolders:
	# 		list_files=os.listdir(os.path.join(parentDirectory,eachSubFolder))
	# 		for file in list_files:
	# 			file_name=eachSubFolder+'/'+file
	# 			# print(file_name)
	# 			sqlStatement="""select expressionID  from TrainDataInfo where filePath='"""+file_name+"""'"""
	# 			cur.execute(sqlStatement)
	# 			rows=cur.fetchall()
	# 			if(len(rows)>0):
	# 				expression=expression_dict[rows[0][0]]
	# 				destination=os.path.join(validationDirectory,expression)
	# 				file_name='_'+str(file_counter)+'.jpg'
	# 				destination=os.path.join(destination,file_name)
	# 				print(file,expression)
	# 				source=os.path.join(parentDirectory,eachSubFolder)
	# 				source=os.path.join(source,file)
	# 				copyfile(source,destination)
	# 				file_counter+=1
	# 			# print(rows[0])
				# print(expression_dict[rows[0]])

	for item in categories:
		dataFolder=os.path.join(parentDirectory,item)
		des_1_dir=os.path.join(trainDirecotry,item)
		des_2_dir=os.path.join(validationDirectory,item)
		list_files=os.listdir(dataFolder)
		train_files=list_files[0:int(0.8*len(list_files))]
		validation_files=list_files[int(0.8*len(list_files)):]
		for item in train_files:
			print(item)
			copyfile(os.path.join(dataFolder,item),os.path.join(des_1_dir,item))
		# for item in validation_files:
		# 	print(item)
		# 	copyfile(os.path.join(dataFolder,item),os.path.join(des_2_dir,item))
				
		# print(item,len(list_files))

	# print(len(cat_files),len(dog_files))
	# train_files=cat_files[0:10000]
	# validation_files=cat_files[10000:]
	# train_files.extend(dog_files[0:10000])
	# validation_files.extend(dog_files[10000:])
	# print(len(train_files),len(validation_files))
	# for file in train_files:
	# 	if 'cat' in file.lower():
	# 		copyfile(os.path.join(parentDirectory,file),os.path.join(trainDirecotry,'cats',file))
	# 	if 'dog' in file.lower():
	# 		copyfile(os.path.join(parentDirectory,file),os.path.join(trainDirecotry,'dogs',file))
	
	# for file in validation_files:
	# 	if 'cat' in file.lower():
	# 		copyfile(os.path.join(parentDirectory,file),os.path.join(validationDirectory,'cats',file))
	# 	if 'dog' in file.lower():
	# 		copyfile(os.path.join(parentDirectory,file),os.path.join(validationDirectory,'dogs',file))



	# print(list_files)
if __name__ == '__main__':
	preprareData()