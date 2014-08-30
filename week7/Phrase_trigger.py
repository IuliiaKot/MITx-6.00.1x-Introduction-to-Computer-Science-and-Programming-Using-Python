# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, and PhraseTrigger in this box
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
        
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        return self.phrase in story.getSubject() or self.phrase in story.getTitle() or self.phrase in story.getSummary()