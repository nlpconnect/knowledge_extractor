# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_token_based_ke.ipynb (unless otherwise specified).

__all__ = ['TokenKnowledgeExtractor']

# Cell
import spacy

# Cell
class TokenKnowledgeExtractor:
  """Extract knowledge like token, lemma,pos, tags, noun chunks etc."""
  def __init__(self, spacy_model="en_core_web_sm"):
    try:
      self.nlp = spacy.load(spacy_model)
    except:
      print('Please download en_core_web_sm using your cmd- python -m spacy download en_core_web_sm')

  def __get_token_knowledge(self, doc):
    results = []
    for token in doc:
        token_info = {}
        token_info['token'] = token.text
        token_info['lemma'] = token.lemma_
        token_info['pos'] = token.pos_
        token_info['tag'] = token.tag_
        token_info['is_alpha'] = token.is_alpha
        token_info['is_stop'] = token.is_stop
        results.append(token_info)
    return results

  def __get_noun_chunks_knowledge(self, doc):
    results = []
    for chunk in doc.noun_chunks:
        chunk_info = {}
        chunk_info['chunk'] = chunk.text
        chunk_info['root_text'] = chunk.root.text
        chunk_info['root_dep'] = chunk.root.dep_
        chunk_info['root_head'] = chunk.root.head.text
        results.append(chunk_info)
    return results

  def extract(self, text):
    extracted_info = {
        'raw_text':text
    }
    docs = self.nlp(text)
    sents = docs.sents
    extracted_info["sents"] = []
    for sent in sents:
        sent_info = {}
        sent_info["text"] = sent.text
        sent_info["tokens"] = self.__get_token_knowledge(sent)
        sent_info["noun_chunks"] = self.__get_noun_chunks_knowledge(sent)
        extracted_info["sents"].append(sent_info)
    return extracted_info