#WIP
#Still works though(the code is shit) - "python exsearch.py *"

'''
Use regex search - have to specifcally say that it is a regex or we may not be able to search for a specific regex like expression in the file 
only check in Text or code files and not in files like doc files
Search in multiple files like
	exsearch * (it will search for all files in a folder or someting like that)
'''

import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_if_ex_available(file_to_check, exper):
	'''
	This is the basc function to check if the file has a specific expression
	TODO
	* make it to be able to search with regex
	* create a nice display output like that of git showcasing the part where the specific expression is found
	'''
	#file_obj = open(file_to_ckeck)
	file_text = file_to_check.read()
	if exper in file_text:
		return True
	else:
		return False

def get_lines_with_exper(file_to_check, exper):
	'''
	This funciton gets the file which has already been checked to have the exoression contained in it
	Then the function gives back a list with the line numbers with the occurences of the expression
	It has to return a list a file can contain multiple occurences of the same expression
	'''
	#work out getting lines after the line with the current line which contains the expression
	#But we still wanna check into the possibility that two consecutive lines could have the expression - so just dont loop foreward and find the line
	prev_line = ""
	prev_prev_line = ""
	prev_prev_prev_line = ""
	line_number = 0
	with open(file_to_check.name) as f:
		for line in f:
			line_number = line_number + 1
			if exper in line:
				print   "   " + prev_prev_prev_line + "   " + prev_prev_line + "   " + prev_line + bcolors.WARNING + "(" + str(line_number) + ") " + bcolors.OKGREEN + line + bcolors.ENDC + bcolors.BOLD +"\n\t\t******\n" + bcolors.ENDC
			else:
				prev_prev_prev_line = prev_prev_line
				prev_prev_line = prev_line
				prev_line = line

def generate_output(file_with_exper):
	'''
	This function is used to generate a neat and clean display of when and where the occurence of the specific file is available
	Sample result:
		line before(2 lines)
		the line with the expression (colorful probably)
		line after(2 lines)
		.
		.
		.
		repeat this if a single files has multiple occurences of a single expression
	''' 
	pass


def main():
	parser = argparse.ArgumentParser(description = "Search files for a specific expression")
	parser.add_argument('file', type=argparse.FileType('r'), nargs='+', help = "Files to search for the expression")
	args = parser.parse_args()
	expression = raw_input("Expression : ")
	for file_obj in args.file:
		status = check_if_ex_available(file_obj, expression)
		if status == True:
			#print "Text is available in file " + file_obj.name
			print "\n" + bcolors.OKBLUE + "_________________________   " + bcolors.FAIL + bcolors.BOLD + file_obj.name + bcolors.ENDC +bcolors.OKBLUE + "   _________________________" + bcolors.ENDC + "\n"
			get_lines_with_exper(file_obj, expression)


#Final call and doing the "thing"
if __name__ == '__main__':
	main()