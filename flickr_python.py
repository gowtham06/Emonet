#!/Users/gowthamkannan/anaconda3/bin/python

import flickrapi
import urllib,os
# DIR='FLICKR_DATA'
import urllib.request
def download_image(url,index,domain,folder):
	DIR='FLICKR_DATA'
	if not os.path.exists(DIR):
		os.makedirs(DIR)
		try:
			if not os.path.exists(DIR+'/'+domain):
				os.makedirs(DIR+'/'+domain)
			if not os.path.exists(DIR+'/'+domain+'/'+folder):
				os.makedirs(DIR+'/'+domain+'/'+folder)
			urllib.request.urlretrieve(url,os.path.join(DIR+'/'+domain+'/'+folder,str(index)+'_.jpg'))
		except Exception as e:
			print(e)

api_key='a59f48bfc036e9d0cc2b2d5d270b50f3'
api_secret='976fa6d5317d7972'
flickr=flickrapi.FlickrAPI(api_key,api_secret,cache=True)
keyward='dogs'
keyward_list=['dogs','cats','humans']
emotion_list=['fear','anger','sadness','joy','disguist','surprise','trust','anticipation']
threshold_count=500
keyward='human sad face'
try:
	photos = flickr.walk(text=keyward,tag_mode='all',tags=keyward,extras='url_c',per_page=100)
except Exception as e:
	print(e)

# for index,photo in enumerate(photos):
# 	print(photo)
# 	if(counter<=threshold_count):
# 		try:
# 			url=photo.get('url_c')
# 			if url is not None:
# 				print("URL:%s"%url)
# 				download_image(url,counter,photo,keyward)
# 				counter+=1
# 		except Exception as e:
# 			print('Failed to download image')
# 			print(e)