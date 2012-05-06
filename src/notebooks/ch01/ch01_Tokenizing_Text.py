# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# <h1>Tokenizing Text</h1>

# <markdowncell>

# <h2>Tokenizing Sentences</h2>
# <p>This example uses a toknenizer that is loaded on demand</p>

# <codecell>

para = "Hello World. It's good to see you. Thanks for using NLTK."
from nltk.tokenize import sent_tokenize
sent_tokenize(para)

# <markdowncell>

# <p>If you're going to tokenize many sentences, it is more efficient ot load the tokenizer instance directly from a pickle file.
# The example above uses the PunktSentenceTokenizer, which can be kept in memory as follows
# </p>

# <codecell>

import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = tokenizer.tokenize(para)
sentences

# <markdowncell>

# <h2>Tokenizing Sentences Into Words</h2>
# <p>Here we extend the previous example, by tokeninizing a sentence into words. We can do this by directly tokenizing the paragraph, <em>para</em>, as shown here:</p>

# <codecell>

from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
penn_tokenizer = TreebankWordTokenizer()
words1 = penn_tokenizer.tokenize(para)
words2 = word_tokenize("Hello World.")
words3 = penn_tokenizer.tokenize("Hello World.")
print words1
print words2
print words3

# <markdowncell>

# <p> Or, since we have already broken <em>para</em> into sentences, we can create the word list by tokeninzing each 
#     sentence and creating a <strong>flatmap</strong> as shown here: </p>

# <codecell>

from nltk.tokenize import PunktWordTokenizer
words3 = [word for sentence in sentences for word in word_tokenize(sentence)]
punkt_tokenizer = PunktWordTokenizer()
words4 = [word for sentence in sentences for word in punkt_tokenizer.tokenize(sentence)]
print words3 == words4
print words3
print words4

# <markdowncell>

# <p>Notice that there are <em><strong>subtle differences in the output</em></strong>. The first example did not separate the '<strong>.</strong>' from the words <em>World</em>
#     and <em>you</em> where as the
#     second example did. Both accounted for the '<strong>.</strong>' after <em>NLTK</em>. I'm not sure why this is the case. Notice how both examples resulted in the splitting of
#     <em>It's</em> into two words. It seems that the <strong>TreebankWordTokenizer</strong>, for which <strong>word_tokenizer</strong> is a wrapper, seems to change behavior 
# when working on a whole paragraph versus individual sentences.</p>
# 
# <p>But I don't want contractions split into separate words. Use a <strong>RegexpTokenizer</strong> as shown next:</p>

# <codecell>

from nltk.tokenize import RegexpTokenizer
regex_tokenizer = RegexpTokenizer("[\w']+")
words5 = [word for sentence in sentences for word in regex_tokenizer.tokenize(sentence)]
print words5

# <markdowncell>

# <h2>Filtering <em>Stop</em> Words</h2>
# <p> <em>Stop</em> words are those that effectively don't contribute to the meaning of a sentence, e.g. <em>a</em>. These can be filtered out as
#     follows</p>

# <codecell>

from nltk.corpus import stopwords
english_stops = set(stopwords.words('english'))
filtered_words = [word for word in words5 if word not in english_stops]
print filtered_words

# <markdowncell>

# <h2>Obtaining Synonym Sets (<em>synsets</em>)</h2>
# <p><em>Synsets</em> are, as their name implies sets of words realted by meaning with a well defined heiracheral relationship. A synset has 
#     <em>hypernyms</em> which are related synsets that are less specific in meaning and <em>hyponyms</em> which are words that are more specific in 
#     menaing</p>

# <codecell>

from nltk.corpus import wordnet
syns = wordnet.synsets('fire')
print 'There are ',len(syns), ' synsets for fire'
syn0 = syns[0]
print 'The first is named: ',syn0.name
print 'Notice that it\'s name includes the \"part of speech tag\", or pos: ', syn0.pos
print 'It\'s definition is: ',syn0.definition
print 'It has ',len(syn0.hypernyms()),' hypernym: ', syn0.hypernyms()[0].name
print 'It has ', len(syn0.hyponyms()),' hyponyms'
syn0_hypo_names = [hypo.name for hypo in syn0.hyponyms()]
print 'They are named: ', syn0_hypo_names
print 'The number of synsets and their pos for fire are: verb ',len(wordnet.synsets('fire', pos='v')),', noun'

# <markdowncell>

# <h2>Lemmas, Synonyms, and Antonyms</h2>
# <p>In linguistics, a <strong><em>lemma</em></strong> is the canoncial form of a word. Lemmas can be obtained from a synset. A synset can have
#     multiple lemmas, but a given lemma, will only belong to <strong>one</strong> synset. Lemmas in a given synset are thus synonyms.
# </p>

# <codecell>

fire_2 = wordnet.synsets('fire')[1]
fire_2_lemmas = fire_2.lemmas
print 'The second synset of fire is', fire_2.name
print 'and it\'s meaning is: ', fire_2.definition
print 'It has ',len(fire_2_lemmas),' lemmas'
print 'They are ', [lemma.name for lemma in fire_2_lemmas]

# <markdowncell>

# <p>Some lemmas also have <strong>antonyms</strong>. Notice below that the antonym function returns a collection of Lemma objects. To 
#     obtain the defintion of the antonym (via the Lemma object) is first necessary to obtain the synset from antonym Lemma (see last line)</p>

# <codecell>

good = wordnet.synset('good.n.02')
print good.name,': ', good.definition
not_good = good.lemmas[0].antonyms()[0]
print not_good.name,': ',not_good.synset.definition

# <markdowncell>

# <h2>Comparing Word (SynSet) Similarity</h2>
# <p> Two synsets, i.e. words, can be compared by examining their positions in the hypernym tree. There are (at least?) three methods provided
#     in the NLTK. The Wu-Palmer, Path, and Leacock Chodorow. </p>

# <codecell>

from nltk.corpus import wordnet
cookbook = wordnet.synset('cookbook.n.01')
instruction_book = wordnet.synset('instruction_book.n.01')
print 'Wu-Palmer Similarity = ', cookbook.wup_similarity(instruction_book)
print 'Path Similarity = ', cookbook.path_similarity(instruction_book)
print 'Leacock Chodorow Similarity = ', cookbook.lch_similarity(instruction_book)

