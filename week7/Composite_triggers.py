# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        text = self.replasePunctuation(text)
        return self.word in text.lower().split()

    def replasePunctuation(self, text):
        for i in string.punctuation:
            text = text.replace(i, ' ')
        return text

# TODO: TitleTrigger

class TitleTrigger(WordTrigger):

    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2


    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)
