

### An Example Messenger bot built using Kemosabe

Note: This bot will only run on flasks development server for now. Can't be used with other servers yet.

### Setting things up

#### #001

Creating a python virtual env
```
  mkdir tvshowbot
  virtualenv -p python3 tvshowbot
  cd tvshowbot
  source bin/activate
```

#### #002

Cloning the  git repo

```
git clone https://github.com/HarowitzBlack/Simplebot
```

#### #003

Installing dependencies

```
pip3 install -r requirements.txt
```

### Running the bot

The bot starts running on flasks development server (Shouldn't be used in production).

```
python3 app.py
```

### Exposing the bot to the internet using Ngrok

+ Download [ngrok](https://ngrok.com/) from the official website.

+ In you're terminal or cmd, run ngrok using ``` ./ngrok http 5000```. The 5000 is the port on which ngrok should be running.
  Also tt's the same port on which the bot is running too.  

+ Now, on the terminal you should see some info. Copy the https url to your clipboard.

+ Go to https://developers.facebook.com create an application if you haven't. Then go to the webhook section and click on edit
  subscription button.

+ Add the url and verification token there.

+ Remember to subscribe to the pages. Otherwise you can't message the bot. 
