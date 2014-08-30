# Enter your code for WordTrigger, TitleTrigger, 
# SubjectTrigger, and SummaryTrigger in this box

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

# TODO: SubjectTrigger

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())