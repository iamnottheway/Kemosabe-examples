

import kemosabe

def get_started(session):
    uid = session.id
    kemosabe.send_text_message(uid,"Hello there, I'm Capy! I'm a demo bot designed to ask meaning less questions.")
    # generate payload strings, this triggers the event.
    altered_carbon = kemosabe.create_action(action='team1',type='altered_carbon')
    gameofthrones = kemosabe.create_action(action='team2',type='gameofthrones')
    # each list is a quick reply button
    payload = (
               ["Altered Carbon 👨‍🎤",altered_carbon,"text"], #
               ["Game Of Thrones 🐺",gameofthrones,"text"],
              )
    # send it to the user
    kemosabe.send_quick_reply(uid,"What's your favorite TV show? 📺",payload)

def altered_carbon_cards(session):
    uid = session.id
    cards = {"element_data":[{
                                    "data":
                                    ["Altered Carboon","https://pmcdeadline2.files.wordpress.com/2018/01/alteredcarbon_kovacs_vertical-core_rgb_us.jpg?w=605&h=897",\
                                    "A Netflix Show","https://www.youtube.com/watch?v=dhFM8akm9a4"],\
                                    "button":["web_url","https://www.youtube.com/watch?v=dhFM8akm9a4",\
                                    "watch now"]}
    ]}
    kemosabe.send_card_templates(uid,cards)


def gameofthrones_cards(session):
    uid = session.id
    cards = {"element_data":[{
                                    "data":
                                    ["Jon Snow","https://vignette.wikia.nocookie.net/gameofthrones/images/a/a5/Profile-JonSnow-707.png/revision/latest?cb=20170828030553",\
                                    "Bastard of Winterfell","https://gameofthrones.wikia.com/wiki/Jon_Snow"],\
                                    "button":["web_url","https://gameofthrones.wikia.com/wiki/Jon_Snow",\
                                    "Wikia"]},
                            {
                                    "data":
                                    ["Bran Stark","https://upload.wikimedia.org/wikipedia/en/thumb/f/fa/Bran_Stark_-_Isaac_Hempstead-Wright.jpeg/220px-Bran_Stark_-_Isaac_Hempstead-Wright.jpeg",\
                                    "Son of Ned Stark","https://gameofthrones.wikia.com/wiki/Bran_Stark"],\
                                    "button":["web_url","https://gameofthrones.wikia.com/wiki/Bran_Stark",\
                                    "Wikia"]},
    ]}
    kemosabe.send_text_message(uid,"Who's your favorite character?")
    kemosabe.send_card_templates(uid,cards)

def text(session):
    # echo text back
    uid = session.id
    text = session.text.lower()
    if "help" in text:
        kemosabe.send_text_message(uid,"Tap on the start over button")
    else:
        kemosabe.send_text_message(uid,text)
