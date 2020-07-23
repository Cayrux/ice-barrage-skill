from mycroft import MycroftSkill, intent_file_handler


class IceBarrage(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('barrage.ice.intent')
    def handle_barrage_ice(self, message):
        self.speak_dialog('barrage.ice')


def create_skill():
    return IceBarrage()

