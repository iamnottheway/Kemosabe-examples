

### Example bots built using Kemosabe for Messenger





### Setting things up

#### #001

Creating a python virtual env
```
  mkdir tvshowbot

  virtualenv -p python3 bots

  cd bots

  source bin/activate
```

#### #002

Cloning the  git repo

```
git clone https://github.com/HarowitzBlack/kemosabe
```

#### #003

Installing dependencies

```
pip3 install -r requirements.txt
```

### Running the bot

cd into any bot folder and run `app.py`. Remember to set the congifs in the app.py, this will automatically
update the configs in configs.json.

Note: The bot will run using Gunicorn.

```
python3 app.py
```

### Exposing the bot using Ngrok

+ Download [ngrok](https://ngrok.com/) from the official website.

+ In you're terminal or cmd, run ngrok using ``` ./ngrok http 5000```. The 5000 is the port on which ngrok should be running.
  Also it's the same port on which the bot is running too. If you used some other port set it to that.

![terminal](https://github.com/HarowitzBlack/Simplebot/blob/master/images/terminal.png)

+ Now, in the terminal you should see some info. Copy the https url to your clipboard.

![Dev](https://github.com/HarowitzBlack/Simplebot/blob/master/images/dev.png)

+ Go to https://developers.facebook.com create an application if you haven't. Then go to the webhook section and click on edit
  subscription button.

+ Add the webhook url and verification token there. `/hook` will be receiving all the JSON responses, so remember to add `/hook`
  at the end of the url.
  ```
  https//:whateverurl/hook
  ```

+ Also remember to subscribe to the pages. Otherwise you can't message the bot.
