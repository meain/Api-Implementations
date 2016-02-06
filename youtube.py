'''
This is used to get comments of a youtube video by providing the video id
'''

from apiclient.discovery import build

#Give your api key here, you can obtain it by using the google api console (https://console.developers.google.com)
#And btw the number of requests using an api key will be limited
api_key = 'your-api-key'

#authenticate
youtube = build('youtube', 'v3', developerKey = api_key)

#request and obtain youtube comments - video_id -- id of the youtube video
def get_youtube_comments(video_id):
	results = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText"
  ).execute()
	return results

def display_comments(comment_querry_result):
	for item in res["items"]:
		#author name
		print item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"] + " :"
		#author comment
		print item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
		print "\n\n"


# Get to display comments of a video by giving the videoId(silly google, they dont have python naming scheme)
vid = ''	#id of the youtube video
res = get_youtube_comments(vid)
display_comments(res)