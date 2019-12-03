import requests
import re
import html

# Input user for a Memrise URL and the number of pages
url = str(input('Please enter a Memrise URL (e.g.: https://www.memrise.com/course/1180494/spanish-mexico-1/): '))
num = None

# When wrong number is given handle error
try:
	num = int(input('Please enter a number to use in the URL: '))
except:
	raise SystemExit('Please provide a valid integer')

res = []
print('Gathering the words from the given URL...')

# Loop through the URLs and gather the words using RegExp
for i in range(1, num + 1):
	try:
		response = requests.get(url + str(i))
	except:
		raise SystemExit('The URL given is invalid')
	cont = response.text
	pattern1 = re.compile('<div class="col_a col text"><div class="text">(.+?)<')
	pattern2 = re.compile('<div class="col_b col text"><div class="text">(.+?)<')
	match = pattern1.findall(cont)
	trans = pattern2.findall(cont)
	tmp = list(zip(match, trans))
	tst = [s1 + ' - ' + s2 for s1, s2 in tmp]
	res += tst
	print('URL No.', str(i) ,'is done')

print('Successfully collected every word')

# Output result as a string of [foreign_word]-[meaning]
for el in res:
	if res.index(el) == len(res) - 1:
		print(html.unescape(el))
	else:
		print(html.unescape(el) + ', ', end='')
