

import kemosabe,views,json


bot = kemosabe.Kemosabe()
bot.set_keys(api_key="<api_key>",
                      verify_key="<verify_key>")

events = {
    "@get_started":views.get_started,
    "@fallback":views.fallback,
    "@get_coffee":views.get_coffee,
    "@get_tea":views.get_tea,
    "@show_fact":views.show_fact,
}

bot.set_events(events)

simple_menu = json.loads(open("configs.json").read())

if __name__ == "__main__":
    bot.run(port=5622,debug=True,set_menu=simple_menu)
