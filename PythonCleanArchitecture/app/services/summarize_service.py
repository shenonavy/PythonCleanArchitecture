
import spacy
import pytextrank

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("textrank")

class SummarizeService:

    def get_summery(self, text):
        doc = nlp(text)
        summery = ''
        for sent in doc._.textrank.summary(limit_sentences=1):
            summery += str(sent)
        return summery