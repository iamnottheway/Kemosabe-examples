

import kemosabe

def get_started(session):
    uid = session.id
    kemosabe.send_text_message(uid,"Hello there, I'm Capy! I'm a demo bot designed to ask meaning less questions.")
    # generate payload strings
    espresso = kemosabe.create(action='get_coffee',type='espresso')
    cappuccino = kemosabe.create(action='get_coffee',type='capp')
    green_tea = kemosabe.create(action='get_tea',type='green')
    lemon_tea = kemosabe.create(action='get_tea',type='lemon')
    # each list is a quick reply button
    payload = (["Espresso ☕️",espresso,"text"],
               ["Cappuccino ☕️",cappuccino,"text"],
               ["Green Tea 🍵",green_tea,"text"],
               ["Lemon Tea 🍋",lemon_tea,"text"],
              )
    # send it to the user
    kemosabe.send_quick_reply(uid,"What's your favorite beverage? 😋",payload)

def get_coffee(session):
    uid = session.id
    if session.type == "espresso":
        kemosabe.send_text_message(uid,"You have good taste kemosabe.")
    else:
        yes = kemosabe.create(action='show_fact',milk_yes=True)
        no  = kemosabe.create(action='show_fact',milk_yes=False)
        payload = (["Yes",yes,"text"],
                   ["No",no,"text"],
                  )
        kemosabe.send_quick_reply(uid,"So you like milk? 🥛",payload)

def get_tea(session):
    uid = session.id
    if session.type == "lemon":
        cards = {"element_data":[{"data":
                                        ["Lemon Tea","https://www.drkarafitzgerald.com/wp-content/uploads/2016/02/spicytea-e1455826441744.jpg",\
                                        "Lemon Tea is good","https://www.wikihow.com/Prepare-Lemon-Tea"],\
                                        "button":["web_url","https://www.wikihow.com/Prepare-Lemon-Tea",\
                                        "Wiki How"]},
                ]}
        kemosabe.send_text_message(uid,"Here's an article on green tea")
        kemosabe.send_card_templates(uid,cards)
    else:
        kemosabe.send_text_message(uid,"Lemon tea is healthy.")

def show_fact(session):
    uid = session.id
    if session.milk_yes:
        kemosabe.send_text_message(uid,"Great! I love milk too")
    else:
        kemosabe.send_text_message(uid,"So, you're the mature type.")


def fallback(session):
    # echo text back
    uid = session.id
    text = session.text.lower()
    if "help" in text:
        kemosabe.send_text_message(uid,"Tap on the start over button")
    else:
        kemosabe.send_text_message(uid,text)
