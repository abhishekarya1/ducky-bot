from flask import *
import praw
import random
  
app = Flask(__name__)  

reddit = praw.Reddit(client_id='ityEzWc1Ds4_Fw',
                     client_secret='testToken', 
                     password="testPass",
                     user_agent='test',
                     username='testUser')


@app.route('/debug')
def debug():
	return "<h1> Working!</h1>";


# image subs
@app.route('/meme')  
def meme():
	i = 1
	while(i):
		i = 0
		meme = reddit.subreddit("memes+dankmemes").random()
		submission = meme.url
		if meme.over_18 == False:									#nsfw filter
			return f"<img src={submission} width=\"500\">"
		else:
			i = 1

@app.route('/puppy')  
def puppy():
	pup = reddit.subreddit("rarepuppers").random()
	submission = pup.url
	return f"<img src={submission} width=\"600\">"

@app.route('/art')  
def art():
	art = reddit.subreddit("art+artporn").random()
	title = art.title
	link = art.shortlink
	submission = art.url
	return f"<img src={submission} width=\"1280\"> <h3>{title}</h3>  <a href =\"{link}\">🔗 {link}</a>"

@app.route('/wallpaper')  
def wallpaper():
	wallpaper = reddit.subreddit("wallpaper").random()
	title = wallpaper.title
	link = wallpaper.shortlink
	submission = wallpaper.url
	return f"<img src={submission} width=\"1280\"> <h3>{title}</h3> <a href =\"{link}\">🔗 {link}</a>"

@app.route('/whoa')  
def whoa():
	whoa = reddit.subreddit("interestingasfuck+whoadude").random()
	title = whoa.title
	submission = whoa.url
	return f"<img src={submission} width=\"600\"> <h3>{title}</h3>"

@app.route('/itemshop')  
def itemshop():
	item = reddit.subreddit("itemshop").random()
	title = item.title
	submission = item.url
	return f"<img src={submission} width=\"600\"> <h3>{title}</h3>"

@app.route('/comic')  
def comics():
	comic  = reddit.subreddit("comics+webcomics").random()
	title = comic.title
	link = comic.shortlink
	submission = comic.url
	return f"<img src={submission} width=\"600\"> <h3>{title}</h3> <a href =\"{link}\">🔗 {link}</a>"

# text subs
@app.route('/quote')  
def quote():
	quote = reddit.subreddit("quotesporn+quotes").random()
	title = quote.title
	return f"<q>{title}</q>"

@app.route('/showerthots')
def showerthoughts():
	showerthought  = reddit.subreddit("showerthoughts").random()
	title = showerthought.title
	return f"<p>{title}</p>"

@app.route('/scary')  
def twosentencehorror():
	story  = reddit.subreddit("twosentencehorror").random()
	title = story.title
	body = story.selftext
	return f"<p>{title}</p> <p>{body}</p>"

@app.route('/test')  
def test():
	submissions = list(reddit.subreddit('memes').hot(limit = 60))
	quote = random.choice(submissions)
	title = quote.title
	return f"<q>{title}</q>"


#main
if __name__ =='__main__':
    app.run(debug = True)  
