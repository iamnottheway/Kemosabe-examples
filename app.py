

import kemosabe,views
import json

events = {
    "@get_started":views.get_started,
    "@text":views.text,
    "@team1":views.altered_carbon_cards,
    "@team2":views.gameofthrones_cards
}

# set events
bot = kemosabe.Kemosabe(events)
# set keys here. Changing keys here will also update the keys in configs.json file.
bot.set_keys(api_key="EAAIggdPYmhYBAAaMv8vD0f3tq5KjBRpqa6mapytuovLtNVIt1NURBc5L5g6ZCTIRQyOLOZAbTd5ay2ytKjr4ac5d4OrpKX5fzo1lCEj6JVsVF7iF6gEvL3TV0p6ke1KOK8MuDrSyLM8UOn6AEgwldYCKHdEFxKpZAy0oc4D9wZDZD",verify_key="bot")
# menu enables text field. Anything typed into it will trigger the @text event.
menu = json.loads(open("menu.json").read())

if __name__ == "__main__":
    bot.run(port=5000,debug=True,set_menu=menu)
