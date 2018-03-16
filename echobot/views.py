
import kemosabe

def get_started(session):
    uid = session.id
    kemosabe.send_text_message(uid,"Greetings")

def text(session):
    uid = session.id
    msg = session.text
    kemosabe.send_text_message(uid,msg)
