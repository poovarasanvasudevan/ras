from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.extractors import EntityExtractor
import logging
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os

logger = logging.getLogger(__name__)


class NerEntityExtractor(EntityExtractor):
    name = "core_ner"
    provides = ["entities"]

    def process(self, message, **kwargs):
        tagger = StanfordNERTagger('C:\\Users\\iampo\\PycharmProjects\\RasaBot\\core\\english.all.3class.distsim.crf.ser.gz',
                                   'C:\\Users\\iampo\\PycharmProjects\\RasaBot\\core\\stanford-net.jar')
        tokenized_text = word_tokenize(message.text)
        classified_text = tagger.tag(tokenized_text)
        logger.info(message.text)

        for x in classified_text:
            print(x)

    @staticmethod
    def extract_entities(doc):
        entities = [
            {
                "entity": ent.label_,
                "value": ent.text,
                "start": ent.start_char,
                "confidence": None,
                "end": ent.end_char
            }
            for ent in doc.ents]
        return entities
