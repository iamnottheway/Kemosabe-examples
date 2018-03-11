

import kemosabe,views
import json

events = {
    "@get_started":views.get_started,
    "@text":views.text,
    "@team1":views.altered_carbon_cards,
    "@team2":views.gameofthrones_cards
}

# set events
bot = kemosabe.Kemosabe(esvents)
# set keys here. Changing keys here will also update the keys in configs.json file.
bot.set_keys(api_key="<apikey>",verify_key="<verify_key>")
# menu enables text field. Anything typed into it will trigger the @text event.
menu = json.loads(open("menu.json").read())

if __name__ == "__main__":
    bot.run(port=5000,debug=True,set_menu=menu)
