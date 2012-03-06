from gnosis.indexer import TextSplitter
from nltk.probability import *
from nltk.stem.porter import PorterStemmer

def stopwords():
  """English language stopwords to be removed from sentences"""
  
  return ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "can", "can't", "will", "like", "one", "just", "don't", "do", "much", "little", "now", "good", "new", "really", "real", "see", "lots", "lot", "comments", "comment", "never", "always", "also", "let's", "lets", "quot"]

def get_th():
  """Threshold percentage used to determine if two pieces of text are related to one another.  You might need to modify this value to fit your needs."""
  
  return 35

def is_numeric(str):
  """Determines if a string str is a numeric value."""
  
  try:
    i = float(str)
  except ValueError, TypeError:
    return False
  else:
    return True

def get_tags(text):
  """Tags every word in a piece of text to determine if each word is a verb, sustantive, adjective, etc."""
  
  import nltk

  tokenizer = nltk.tokenize.RegexpTokenizer(r'''[\w']+|[^\w\s]+''')
  tagger = nltk.UnigramTagger(nltk.corpus.brown.tagged_sents())

  tokenized = tokenizer.tokenize(text)
  tagged = tagger.tag(tokenized)
  tagged.sort(lambda x,y:cmp(x[1],y[1]))
  return tagged

def get_stems(text):
  """Stems every word in a piece of text."""
  
  sw = stopwords()
  sw_stems = []

  stemmer = PorterStemmer()
  article = TextSplitter().text_splitter(text)
  stems = FreqDist()

  for word in sw:
    sw_stems.append(stemmer.stem(word.decode('utf8')))

  for word in article:
    try:
      sw_stems.index(stemmer.stem(word.lower()))
    except ValueError:
      if(not is_numeric(word)):
        stems.inc(stemmer.stem(word.lower()))

  word_stems = stems.samples()
  word_stems.sort()
  word_stems[60:80]
  return word_stems

def compare(txt1, txt2):
  """Compares two texts.  Returns True if they're related."""
  
  percent = get_comp_rate(txt1, txt2)

  if(percent >= get_th()):
    return True

def get_comp_rate(txt1, txt2):
  """Returns the similarity in percentage between two texts."""
  
  stems = get_stems(txt1)
  stems_comp = get_stems(txt2)
  
  if(len(stems_comp) > len(stems)):
    total_stems = len(stems)
    longer_stems = stems_comp
    shorter_stems = stems
  else:
    total_stems = len(stems_comp)
    longer_stems = stems
    shorter_stems = stems_comp

  found_stems = 0

  for word in shorter_stems:
    try:
      longer_stems.index(word)
      if(found_stems < total_stems):
        found_stems += 1
    except ValueError:
      pass

  if(total_stems > 0):
    percent = float(found_stems) / float(total_stems) * 100
  else:
    percent = 0

  return percent

def compare_test(txt1='Is this text', txt2='Similar to this text?'):
  """Compare test."""
  
  rel = compare(txt1, txt2)
  percent = get_comp_rate(txt1, txt2)

  if(rel):
    print("Related: %(percent)f" % {'percent':percent})
  else:
    print("Not related: %(percent)f" % {'percent':percent})