from mycroft import MycroftSkill, intent_file_handler


class TomTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.tom.intent')
    def handle_test_tom(self, message):
        self.speak_dialog('test.tom')


def create_skill():
    return TomTest()

