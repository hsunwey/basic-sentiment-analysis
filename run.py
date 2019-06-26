import plotly.plotly as py
from plotly.graph_objs import *
import extract

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
url11 = "http://www.bbc.com/news/world-asia-43985623"
url12 = "https://www.bbc.com/news/world-asia-44063736"
url = url12

text = extract.extractContent(url)
# print(text)
positiveList = []
negativeList = []
stopList = []
positiveDict = {}
negativeDict = {}
stopDict = {}

neWords = []
poWords = []
stopWords = []
neuWords = []
d = 256
q = 23

# crawlpage method
# print(extract.extractContent(url))
# # Word count Option 1
# print(extract.sortedDictionary(extract.extractContent(url)))

# # Word count Option 2
# print(extract.totalWordCount(extract.extractContent(url)))
# # Word count Option 3
# print(extract.uniqueWordCount(extract.extractContent(url)))

def convertText(openFile, listToAppend):
    myFile = open(openFile)
    fileList = myFile.readlines()
    i=0
    for line in fileList:
        listToAppend.append(fileList[i].replace('\n','').replace(' ','').lower())
        i += 1
    myFile.close()

def createDict(list, dict):
    key = 0
    n = 0
    for i in list:
        s = list[n]
        temp = 0
        for j in range(0,len(s)):
            temp = temp + ord(s[j])
        key = (d*temp)%q
        try:
            dict[key].append(n)
        except KeyError:
            dict[key] = [n]
        n += 1

def checkMatch(s,key1,n):
    if(n == 1):
        for key in positiveDict.keys():
            if key1 == key:
                list1 = positiveDict[key1]
                i = 0
                for item in list1:
                    if positiveList[list1[i]] == s:
                        poWords.append(s)
                        return True
                    i += 1
    elif(n == 2):
        for key in negativeDict.keys():
            if key1 == key:
                list1 = negativeDict[key1]
                i = 0
                for item in list1:
                    if negativeList[list1[i]] == s:
                        neWords.append(s)
                        return True
                    i += 1
    elif(n == 3):
        for key in stopDict.keys():
            if key1 == key:
                list1 = stopDict[key1]
                i = 0
                for item in list1:
                    if stopList[list1[i]] == s:
                        stopWords.append(s)
                        return True
                    i += 1
    else:
        return False

def plotHistogram(listOne, listTwo, listThree):
    trace1 = {
      "x": listOne,
      "marker": {"color": "rgb(44, 160, 44)"},
      "name": "Positive Word",
      "opacity": 0.75,
      "showlegend": True,
      "type": "histogram",
      "xaxis": "x1"
    }
    trace2 = {
      "x": listTwo,
      "marker": {"color": "rgb(31, 119, 180)"},
      "name": "Negative Word",
      "opacity": 0.75,
      "showlegend": True,
      "type": "histogram",
      "xaxis": "x1"
    }
    trace3 = {
      "x": listThree,
      "marker": {"color": "rgb(255, 127, 14)"},
      "name": "Neutral Word",
      "opacity": 0.75,
      "showlegend": True,
      "type": "histogram",
      "xaxis": "x1"
    }
    trace4 = {
      "x": [len(listOne)],
      "marker": {"color": "rgb(44, 160, 44)"},
      "name": "Positive Word",
      "opacity": 0.75,
      "showlegend": True,
      "type": "bar",
      "xaxis": "x2"
    }
    trace5 = {
      "x": [len(listTwo)],
      "marker": {"color": "rgb(31, 119, 180)"},
      "name": "Negative Word",
      "opacity": 0.75,
      "showlegend": True,
      "type": "bar",
      "xaxis": "x2"
    }
    trace6 = {
      "x": [len(listThree)],
      "marker": {"color": "rgb(255, 127, 14)"},
      "name": "Neutral Words",
      "opacity": 0.75,
      "showlegend": True,
      "type": "bar",
      "xaxis": "x2"
    }
    # data = Data([trace1, trace2, trace3, trace4, trace5, trace6])
    data = Data([trace1, trace2, trace4, trace5, trace6])
    layout = {
      # "barmode": "overlay",
      "title": "Sentiment Analysis",
      "xaxis": {
        "domain": [0, 0.6],
        "title": "words count"
      },
      "xaxis2": {
        "domain": [0.65, 1],
        "title": "total word count"
      },
      # "xaxis3": {
      #   "domain": [0.55, 0.75],
      #   "title": "petal length (cm)"
      # },
      # "xaxis4": {
      #   "domain": [0.8, 1],
      #   "title": "petal width (cm)"
      # },
      "yaxis": {"title": "count"}
    }
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)

def rabinKarp():
    key = 0
    numP = 0
    numN = 0
    count = 0
    for i in text:
        temp = 0
        invalid = False
        s = text[count]
        for j in range(0,len(s)):
            temp = temp + ord(s[j])
        key = (d*temp)%q
        invalid = checkMatch(s,key,3)
        if not invalid:
            if checkMatch(s, key, 1):
                numP += 1
                count += 1
                continue
            elif checkMatch(s, key, 2):
                numN += 1
                count += 1
                continue
            else:
                neuWords.append(s)
        count += 1


    print("Positive Words Number is "+str(numP))
    print("Negative Words Number is "+str(numN))
    if(numP>numN):
        print("The content is positive")
    elif(numN>numP):
        print("The content is negative")
    else:
        print("The content is neutral")
    plotHistogram(poWords, neWords, neuWords)
    # plotBar(numP, numN)
    # plotPie(numP, numN)

def plotPie(label, value):
    labels = label
    values = value
    trace = Pie(labels=labels, values=values)
    py.plot([trace], filename='basic_pie_chart')

def plotBar(label, value):
    data = [Bar(
        x = label,
        y = value,
        text = value,
        textposition = 'auto',
        marker=dict(
            color='rgb(158,202,225)',
            line=dict(
                color='rgb(8,48,107)',
                width=1.5),
        ),
        opacity=0.6
    )]
    py.plot(data, filename = 'bar-direct-labels')

def viewWords():
    total = extract.totalWordCount(extract.extractContent(url))
    plotBar(['Total Word', 'Stop Words'], [total, len(stopWords)])



def main():
    convertText("positive.txt", positiveList)
    convertText("negative.txt", negativeList)
    convertText("stopwords_en.txt", stopList)

    createDict(positiveList, positiveDict)
    createDict(negativeList, negativeDict)
    createDict(stopList, stopDict)
    rabinKarp()
    viewWords()
    # print(positiveList)
    # print(negativeList)
    # print(stopList)

main()
