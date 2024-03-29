import discord

import praw

import random

from discord.ext import commands, tasks

from datetime import datetime as dt
import pytz

import json, requests

from prsaw import RandomStuff

import re

reddit = praw.Reddit(client_id='ityEzWc1Ds4_Fw',
                     client_secret='testToken', 
                     password="testPass",
                     user_agent='test',
                     username='testUser',
                     check_for_async=False)


client = commands.Bot(command_prefix = ".")

def setup(bot):
    bot.remove_command("help")
#run to remove "help" command    
setup(client)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"with your feelings | .help"))
    print("Bot ready!")

@client.command()
async def hello(ctx):
	await ctx.send("Hi!")

@client.command()
async def help(ctx):
	embed = discord.Embed(title = "🦆 Duck4u Help", description = "Here are all the available commands: ", color = discord.Colour.green())
	embed.add_field(name = ".help", value = "lists all commands and info", inline = True)
	
	embed.add_field(name = ".meme [hot]", value = "funny meme", inline = True)
	embed.add_field(name = ".puppy", value = "cute dog picture", inline = True)
	embed.add_field(name = ".itemshop", value = "real-world fantasy items", inline = True)
	embed.add_field(name = ".whoa [hot]", value = "stuff that makes you go \"whoa!\"", inline = True)
	embed.add_field(name = ".comic [hot]", value = "witty comic", inline = True)
	embed.add_field(name = ".art [hot]", value = "beautiful art", inline = True)
	embed.add_field(name = ".wallpaper [hot]", value = "stunning wallpaper", inline = True)

	embed.add_field(name = ".showerthot [hot]", value = "thoughts that only come in shower", inline = True)
	embed.add_field(name = ".scary [hot]", value = "two sentence horror", inline = True)
	embed.add_field(name = ".quote", value = "inspirational quotes", inline = True)

	embed.add_field(name = "❗", value = "[hot] is optional, better content though")

	embed.set_footer(text=f"✨ made on a lazy Sunday morning by dFuZeR. Also, {ctx.author.display_name} is a noob.")

	await ctx.send(embed=embed)
	print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : help shown")

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("That command doesn't exists. See `.help` for more info.")
		print(f"ERROR: {dt.now(pytz.timezone('Asia/Kolkata'))}:  Command not found.")

@client.command()
async def meme(ctx, *, arg=None):
	i = 1
	while(i):
		i = 0
		if(arg == "hot"):
			submissions = list(reddit.subreddit('memes+dankmemes').hot(limit = 50))
			meme = random.choice(submissions)
		else:
			meme = reddit.subreddit("memes+dankmemes").random()
		title = meme.title
		submission = meme.url
		if meme.over_18 == False:			#nsfw filter
			em = discord.Embed(title = title)
			em.set_image(url = submission)
			try:
				await ctx.send(embed = em)
				print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : meme fetched : {ctx.author.display_name}") 
			except:
				print(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : meme not fetched : {ctx.author.display_name}")
		else:
			i = 1


@client.command()
async def puppy(ctx):
	pup = reddit.subreddit("rarepuppers").random()
	title = pup.title
	submission = pup.url
	em = discord.Embed(title = title)
	em.set_image(url = submission)
	try:
		await ctx.send(embed = em)
		print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : puppy fetched : {ctx.author.display_name}")
	except:
		print(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : puppy not fetched : {ctx.author.display_name}")


@client.command()
async def art(ctx, *, arg = None):
	i = 1
	while(i):
		i = 0
		if(arg == "hot"):
			submissions = list(reddit.subreddit('art+artporn').hot(limit = 20))
			art = random.choice(submissions)
		else:
			art = reddit.subreddit("art+artporn").random()
		if art.over_18 == False:		#nsfw filter
			title = art.title
			link = art.shortlink
			submission = art.url
			em = discord.Embed(title = title, description = link)
			em.set_image(url = submission)
			try:
				await ctx.send(embed = em)
				print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : art fetched : {ctx.author.display_name}")
			except:
				print(f"FAILURE: art not fetched : {dt.now(pytz.timezone('Asia/Kolkata'))} : {ctx.author.display_name}")
		else:
			i = 1

@client.command()
async def wallpaper(ctx, *, arg = None):
	if(arg == "hot"):
		submissions = list(reddit.subreddit('wallpaper+imaginarysliceoflife').hot(limit = 20))
		wallpaper = random.choice(submissions)
	else:
		wallpaper = reddit.subreddit("wallpaper+imaginarysliceoflife").random()
	title = wallpaper.title
	link = wallpaper.shortlink
	submission = wallpaper.url
	em = discord.Embed(title = title, description = link)
	em.set_image(url = submission)
	try:
		await ctx.send(embed = em)
		print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : wallpaper fetched : {ctx.author.display_name}")
	except:
		print(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : wallpaper not fetched : {ctx.author.display_name}")

@client.command()
async def whoa(ctx, *, arg= None):
	if(arg == "hot"):
		submissions = list(reddit.subreddit('interestingasfuck+whoadude').hot(limit = 20))
		whoa = random.choice(submissions)
	else:
		whoa = reddit.subreddit("interestingasfuck+whoadude").random()
	title = whoa.title
	submission = whoa.url
	em = discord.Embed(title = title)
	em.set_image(url = submission)
	try:
		await ctx.send(embed = em)
		print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : whoa fetched : {ctx.author.display_name}")
	except:
		print(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : whoa not fetched : {ctx.author.display_name}")

@client.command()
async def itemshop(ctx):
	item = reddit.subreddit("itemshop").random()
	title = item.title
	submission = item.url
	em = discord.Embed(title = title)
	em.set_image(url = submission)
	try: 
		await ctx.send(embed = em)
		print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : itemshop fetched : {ctx.author.display_name}")
	except:
		print(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : itemshop not fetched : {ctx.author.display_name}")

@client.command()
async def comic(ctx, *, arg = None):
	if(arg == "hot"):
		submissions = list(reddit.subreddit('comics+webcomics').hot(limit = 20))
		comic = random.choice(submissions)
	else:
		comic  = reddit.subreddit("comics+webcomics").random()
	title = comic.title
	link = comic.shortlink
	submission = comic.url
	em = discord.Embed(title = title, description = link)
	em.set_image(url = submission)
	try:
		await ctx.send(embed = em)
		print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : comic fetched : {ctx.author.display_name}")
	except:
		print(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : comic not fetched : {ctx.author.display_name}")

@client.command()
async def quote(ctx):
	quote = reddit.subreddit("quotesporn+quotes").random()
	title = quote.title
	em = discord.Embed(title = title)
	await ctx.send(embed = em)
	try:
		print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : quote fetched : {ctx.author.display_name}")
	except:
		printf(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : quote not fetched : {ctx.author.display_name}")

@client.command()
async def showerthot(ctx, *, arg = None):
	if(arg == "hot"):
		submissions = list(reddit.subreddit('showerthoughts').hot(limit = 30))
		showerthought = random.choice(submissions)
	else:
		showerthought  = reddit.subreddit("showerthoughts").random()
	title = showerthought.title
	em = discord.Embed(title = title)
	try:
		await ctx.send(embed = em)
		print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : showerthot fetched : {ctx.author.display_name}")
	except:
		printf(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : showerthot not fetched : {ctx.author.display_name}")

@client.command()
async def scary(ctx, *, arg=None):
	if(arg == "hot"):
		submissions = list(reddit.subreddit('twosentencehorror').hot(limit = 30))
		story = random.choice(submissions)
	else:
		story  = reddit.subreddit("twosentencehorror").random()
	title = story.title
	body = story.selftext
	em = discord.Embed(title = title, description = body, color = discord.Colour.red())
	await ctx.send(embed = em)
	try:
		print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : scary fetched : {ctx.author.display_name}")
	except:
		printf(f"FAILURE: {dt.now(pytz.timezone('Asia/Kolkata'))} : scary not fetched : {ctx.author.display_name}")		

# secret commands

@client.command()
async def priash(ctx):
	link = "https://i.imgur.com/HGDRtZ4.jpg"
	em = discord.Embed(title = "macchi", description = "🐟🐟🐟", color = discord.Colour.blue())
	em.set_image(url = link)
	await ctx.send(embed = em)
	print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : priass ran")

@client.command()
async def dudeop(ctx):
	link = "https://media1.tenor.com/images/9413ffc5a11722a3cc456a88810750bd/tenor.gif"
	em = discord.Embed(title = "sedlyf", description = "crie", color = discord.Colour.red())
	em.set_image(url = link)
	await ctx.send(embed = em)
	print(f"SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : dudeop ran")

#memeLoop for auto-memes channel
@tasks.loop(seconds=3600.0)
async def memeLoop():
	channel = client.get_channel(843934951073382480)
	i = 1
	while(i):
		i = 0
		submissions = list(reddit.subreddit('memes+dankmemes').hot(limit = 30))
		meme = random.choice(submissions)
		title = meme.title
		if meme.over_18 == False:			#nsfw filter
			em = discord.Embed(title = title)
			if meme.post_hint == "hosted:video":	#if video, then no embed since Discord API doesn't allow videos in embeds
				try:
					submission = meme.media['reddit_video']['fallback_url']
					await channel.send(title + '\n' + submission.split('?')[0])
					print(f"AUTO SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : video meme fetched automatically") 
				except:
					print(f"AUTO FAIL: {dt.now(pytz.timezone('Asia/Kolkata'))} : video meme not fetched automatically")
			else:
				submission = meme.url
				em.set_image(url = submission)
				try:
					await channel.send(embed=em)
					print(f"AUTO SUCCESS: {dt.now(pytz.timezone('Asia/Kolkata'))} : meme fetched automatically") 
				except:
					print(f"AUTO FAIL: {dt.now(pytz.timezone('Asia/Kolkata'))} : meme not fetched automatically")
		else:
			i = 1
        
memeLoop.start()

@client.command()
async def toss(ctx):
    toss = random.choice(["_**heads**_", "_**tails**_"])
    await ctx.send(toss)
    print(f"TOSS: {dt.now(pytz.timezone('Asia/Kolkata'))} : tossed : {ctx.author.display_name}")


#RandomStuff API for ChatBot
api_key = "randomStuffAPIKey"
rs = RandomStuff(async_mode = True, api_key = api_key)

@client.event
async def on_message(message):
	#don't respond to ourselves
	if message.author == client.user:
		return
	if message.channel.id == channelID and client.user.mentioned_in(message):
		#exclusion of links and gifs
		if message.content.find('http') == -1:
			question = re.sub('<.*?>', '', message.content)	 #to not consider tags and emojis while sending to RandomStuffAPI
			if len(question.strip()) == 0:
				await message.reply("Yo!") #say this when empty message after removing whitespaces
			else:
				response = await rs.get_ai_response(question)
				await message.reply(response[0]['message'])
				print(f"TAG: {dt.now(pytz.timezone('Asia/Kolkata'))} : Chatbot was tagged by {message.author.display_name}")
		else: 
			return	
	elif client.user.mentioned_in(message): #and 'Hi' in message.content:
		url = "https://api.yomomma.info/"
		response = requests.get(url, verify=True)
		await message.reply(response.json()['joke'], mention_author=True)
		print(f"TAG: {dt.now(pytz.timezone('Asia/Kolkata'))} : YoMomma was called by {message.author.display_name}")
	#else:
		#return
	await client.process_commands(message)

client.run('userDiscordToken')
