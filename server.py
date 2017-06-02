import os
from flask import Flask, render_template, request, redirect, session
from urllib2 import Request, urlopen, URLError
# import requests

app = Flask(__name__)

apiKey = "d72d2481a2b84519babe6f85a4b3666e"

apr = requests.get("https://newsapi.org/v1/articles?source=associated-presssortBy=top&apiKey=d72d2481a2b84519babe6f85a4b3666e&sortBy=popular")
ap = urlopen('https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=d72d2481a2b84519babe6f85a4b3666e')


@app.route('/')
def mainIndex():
	print("in 'main'")
	if request.method == 'GET':
		# status = requests.get(apr.status)
		# source = apr.source
		# sortBy = apr.sortBy
		# articles = [apr.author, apr.description, apr.title, apr.url, apr.urlToImage, apr.publishedAt] 
		
		
		response = requests.get("http://placekitten.com/")
		apr = requests.get("https://newsapi.org/v1/articles?source=associated-presssortBy=top&apiKey=d72d2481a2b84519babe6f85a4b3666e&sortBy=popular")
		
		print("{}{}".format("Status: ",apr.status_code))
		print(response.headers)
		print(apr.headers)
		
		
		
	return render_template('index.html', response=response, apr=apr)
	# return render_template('index.html', status=status, source=source, sortBy=sortBy, articles=articles)
	

# start the server
if __name__ == '__main__':
	app.run(host='0.0.0.0', port =80, debug=True)
