'''
This is used to extract conversation only form an srt file
It uses regex to extract the text portion
'''
import re   

f = file("movie srt file")
# Parse the file content
content = f.read()
# Find all result in content
# The first big (__) retrieve the timing, \s+ match all timing in between,
# The (.+) means retrieve any text content after that.
result = re.findall("(\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+)\s+(.+)", content)

#Printing the subtitle actual text portion only 
for item in result:
	print item[1] + "\n" #text (item[0] will be the time)
