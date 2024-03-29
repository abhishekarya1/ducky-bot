### Heroku Deployment Repository 🚀

## Duck4u 🦆
A Discord bot that fetches Reddit posts from subreddits and can run various custom commands for fun.

### Tools 🛠️
- [Python Reddit API Wrapper - PRAW](https://praw.readthedocs.io/)
- [discord.py](https://discordpy.readthedocs.io/)
- python-3.9.0

### Setup and Deploy ⚙️
- Setup virtual environment and activate it
```sh
$ python -m venv venv
$ cd venv/Scripts
$ activate.bat
$ cd ..
$ cd ..
```
- Get Reddit Developer API constants
```txt
App Type: script
URL/URI: http://localhost:8080/
```
- Setting up discord.py
  - create application
  - create a bot
  - get OAuth link
  - open the above link and add bot to a server
  - copy api-key from bot page to code  
  
- Running bot locally
```sh
$ py bot.py
```
- Running on Heroku
1. Create and populate: `Procfile`, `runtime.txt`, `requirements.txt` and place in root of the bot folder alongwith `bot.py`
```sh
$ pip freeze > requirements.txt
```
2. Push to GitHub, create a new app in Heroku and attach to GitHub repository for CI (all via UI)
3. Check build logs in `Deploy -> More -> View logs`
4. Goto `Resources`, specify run command as `py bot.py` and start a dyno. Check logs to make sure its running. Once the bot is ready to accept commands it will output `Bot ready!` on Heroku log console.

### Features 💡
1. Fetch: a random post from specified subreddit, optional [hot] argument fetches a random but "hot" post (w/ NSFW Filter).
2. Custom fun commands: toss a coin, show a gif on named commands.
3. Other: memeLoop, stats system, responds with a custom message on @mention, activity status.

#### Bot Commands 🤖
```txt
hello
help
stats

toss

meme [hot]
puppy
art [hot]
wallpaper [hot]
whoa [hot]
itemshop
comic [hot]

quote
showerthot [hot]
scary [hot]

other hardcoded named commands under `# secret commands`
```
### Technical Aspects 👨‍💻
- Uses embeds for better look and feel
- Custom Loggging: logs `await` success or failure in India Standard Time (GMT+5:30) `pytz`
- memeLoop: Sends a random hot meme to a specified channel every 30mins (w/ NSFW Filter) `random`
- Stats System: TBI `OOP`

### References 📚
- [PRAW Basics with Flask Backend - Medium](https://medium.com/swlh/scraping-reddit-using-python-57e61e322486) (behind signup wall? use Incognito)
- [Code With Swastik - YouTube](https://www.youtube.com/channel/UC2ITRZ4_Di-KMHSIylTQbBA)
- [StackOverflow](https://stackoverflow.com/) (ofcourse!)
- [Deploying to Heroku - dev.to](https://dev.to/p014ri5/making-and-deploying-discord-bot-with-python-4hep)

### Flask App for Testing ⚠️
Flask installation and app file `app.py` is available to test PRAW. Better use [Quart](https://pgjones.gitlab.io/quart/) because of better `async` functionality than Flask.

```sh
$ py app.py
```
