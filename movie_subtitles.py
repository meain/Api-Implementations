'''
This is used to extract conversation only form an srt file
It uses regex to extract the text portion
'''
import re

def get_subtitle_converstions(srt_file):
	f = file(srt_file)
	# Parse the file content
	content = f.read()
	# Find all result in content
	# The first big (__) retrieve the timing, \s+ match all timing in between,
	# The (.+) means retrieve any text content after that.
	result = re.findall("(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\s+(.+)", content)
	conv = []	#initalize as list
	for item in result:
		conv.append(item[1])
	return conv

#Output part
res = get_subtitle_converstions("movie_name.srt")	#Give the name of the srt file here
for cv in res:
	print cv
