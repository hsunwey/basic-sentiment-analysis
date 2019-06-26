import urllib.request
from bs4 import BeautifulSoup

def extractContent(url):
	# return HTTPResponse object
	response = urllib.request.urlopen(url)

	# return in HTML (not prettify version)
	html = response.read()
	start = html.find(b"<body")
	end = html.rfind(b"</footer")

	html = html[start:end]

	# parse the html (not prettify version) to Beautiful soup using "html.parser"
	soup = BeautifulSoup(html,"html.parser")

	# decompose all the things that have belows tags
	if(html.find(b"<script")!= -1):
		for script in soup("script"):
			script.decompose()
	if(html.find(b"<style")!= -1):
		for script in soup("style"):
			script.decompose()
	if(html.find(b"<footer")!= -1):
		for script in soup("footer"):
			script.decompose()
	if(html.find(b"<li")!= -1):
		for script in soup("li"):
			script.decompose()
	if(html.find(b"<br>")!= -1):
		for script in soup("br"):
			script.decompose()
	if(html.find(b"<a")!= -1):
		for script in soup("a"):
			script.decompose()

	# tagName of content that important to extract
	tagName = ['h1','p']
	html_str = ''
	for x in tagName:
		for link in soup.find_all(x):
			html_str += str(link.get_text()) + " "
	return lowerCasePureStr(html_str)

def lowerCasePureStr(html_str):
	pure_str = ""
	counter = 0
	#clear all the space and tap behide the string
	html_str = html_str.rstrip()
	for char in html_str:
		if (char == '-' or char == ' ')and counter == 0:
			if(char == ' '):
				counter += 1
			pure_str += char
		elif char.isalpha():
			counter = 0
			pure_str += char.lower()
	pure_str_list = pure_str.split()
	return pure_str_list

#1. return sortedDictionary word count in the passage
def sortedDictionary(pure_str_list):
	map_list = {}
	for x in pure_str_list:
		if x in map_list.keys():
			map_list[x] += 1
		else:
			map_list[x] = 1

	sorted_map_list ={}
	for key in sorted(map_list.keys()):
		sorted_map_list[key] = map_list[key]
	return sorted_map_list

#2. return total word count in the passage
def totalWordCount(pure_str_list):
	return len(pure_str_list)

#3. return unique word count (not counted duplicated word)
def uniqueWordCount(pure_str_list):
	return len(sortedDictionary(pure_str_list).keys())

if __name__ == '__main__':
	url1 = "http://www.bbc.com/news/world-asia-43851065"
	url2 = "http://www.straitstimes.com/asia/se-asia/pkr-finally-releases-list-of-election-candidates-after-much-tension-among-its-two"
	url3 = "https://www.thestar.com.my/news/nation/2018/04/26/pregnant-driver-terrorised-by-biker-high-on-drugs/"
	url4 = "https://www.thestar.com.my/sport/swimming/2018/04/23/wei-to-go-gan-synchro-swimmer-makes-twomedal-splash-at-china-open/"
	url5 = "http://www.bbc.com/news/world-australia-42867742"
	url6 = "https://www.bbc.com/news/business-14753012"
	url7 = "https://www.nytimes.com/2018/04/02/world/asia/malaysia-fake-news-law.html?rref=collection%2Ftimestopic%2FMalaysia"
	url8 = "https://www.nytimes.com/2018/04/06/world/asia/malaysia-elections-called-najib-razak.html?rref=collection%2Ftimestopic%2FMalaysia"
	url9 = "https://www.bbc.com/news/world-asia-42603220"
	url10 = "https://www.nst.com.my/news/nation/2017/08/274260/countdown-merdeka-treasurewhatwehave"
	url = url1
	# crawlpage method
	print(extractContent(url))
	# Word count Option 1
	print(sortedDictionary(extractContent(url)))
	# Word count Option 2
	print(totalWordCount(extractContent(url)))
	# Word count Option 3
	print(uniqueWordCount(extractContent(url)))
