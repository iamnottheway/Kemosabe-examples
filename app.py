

import kemosabe,views

events = {
    "@get_started":views.get_started,
    "@text":views.text,
    "@team1":views.altered_carbon_cards,
    "@team2":views.gameofthrones_cards
}

# set events
bot = kemosabe.Kemosabe(events)
# set keys here. Changing keys here will also update the keys in configs.json file.
bot.set_keys(api_key="EAAIggdPYmhYBAAlAC2tZC5P4ZAz714WTOhGYZAIIOKYb2SZA2mmhL8FGaNP456RZBuNCBJTpLLjLwKZCZCjxrBIZCElhPcVlpQ1qQlXoHHU9yjGpUX5fcZC91IztxNUWZAKxhEjpVjLLZA2nMFy1zV1whgRkiX261eTlxbJiHe5qO07DQZDZD",verify_key="bot")
# menu enables text field. Anything typed into it will trigger the @text event.
menu = open("menu.json","r").read()

if __name__ == "__main__":
    bot.run(port=5623,debug=True,set_menu=menu)
