from mycroft import MycroftSkill, intent_handler

from translate import Translator as Translate

class Translator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('translator.intent')
    def handle_translator(self, message):
        o_lang = message.data.get('o_lang')
        phrase = message.data.get('phrase')
        
        translator = Translate(provider="mymemory",to_lang=o_lang)
        phrase = translator.translate(phrase)

        self.speak_dialog('translator', data={
            'phrase': phrase
        })


def create_skill():
    return Translator()

