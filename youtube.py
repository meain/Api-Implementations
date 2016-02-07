from apiclient.discovery import build

#Give your api key here, you can obtain it by using the google api console (https://console.developers.google.com)
#And btw the number of requests using an api key will be limited
#Use this to install the tools required :  pip install --upgrade google-api-python-client

api_key = ''	#Give your api key here

#authenticate
youtube = build('youtube', 'v3', developerKey = api_key)


def get_youtube_comments(video_id, max_results = 10):
	'''
	request and obtain youtube comments (top level)
	video_id -- id of the youtube video
	result is a dictionary
	'''
	results = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText",
    maxResults = max_results
  ).execute()
	return results

def get_comment_reply(parent_id, max_results = 10):
	'''
	Function to obtain replies to a comment on youtube video
	parent_id -- id of the main comment
	result is a dictionary
	'''
	results = youtube.comments().list(
    part="snippet",
    parentId=parent_id,
    textFormat="plainText",
    maxResults = max_results
  ).execute()
	return results

def get_parent_id(comment):
	return comment["snippet"]["topLevelComment"]["id"]

'''
Display functions - just for debuging and to show the usage
'''

def display_comment_parent(item):
	#author name (parent)
	print item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"] + " :"
	#author comment (parent)
	print item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

def display_comment_repy(comment_querry_result):
	for items in comment_querry_result["items"]:
		print "\t-----Reply------"
		print "\t" + items["snippet"]["authorDisplayName"]
		print "\t" + items["snippet"]["textDisplay"]


# Get to display comments of a video by giving the videoId(silly google, they dont have python naming scheme)
vid = ''	#id of the youtube video
res_parent = get_youtube_comments(vid)
for items in res_parent["items"]:
	print "\n\n~~~~~~~~~~~~"
	display_comment_parent(items)
	parent_id = get_parent_id(items)
	res_child = get_comment_reply(parent_id)
	if res_child:
		display_comment_repy(res_child)
