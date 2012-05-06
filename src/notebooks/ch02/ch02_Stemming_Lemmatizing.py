# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# <h2>Stemming Words</h2>
# <p>Stemming is the process of removing <em>affixes</em> from a word to obtain it's root, or <em>stem</em>. For example, the stem of <strong>
#     growing</strong> is <strong>grow</strong>. </p>
# <p>Python includes 4 stemming algorithms, 3 of which are demonstrated below. The fourth, <em>Snowball</em> is for non-English languages
#     and is not covered here but is in the text </p>

# <codecell>

from nltk.stem import PorterStemmer, LancasterStemmer, RegexpStemmer
porter = PorterStemmer()
lancaster = LancasterStemmer()
reg = RegexpStemmer('ing')
g = 'growing'
print 'Porter yields: ',porter.stem(g)
print 'lancaster yields: ', lancaster.stem(g)
print 'Regexp yields: ', reg.stem(g)

# <markdowncell>

# <p>The output of various words can be different between stemmers:</p>

# <codecell>

g = 'cookery'
print 'Porter yields: ',porter.stem(g)
print 'lancaster yields: ', lancaster.stem(g)
print 'Regexp yields: ', reg.stem(g)

# <markdowncell>

# <h2>Lemmatizing</h2>
# <p>Lemmatization is similar to stemming, but rather than using some sort of pattern matching, it relies on word hierarchies and meaning,
#     although this is not explained so far in the text. The main practical difference seems to be that lemmitization always produces a 
#     valid word, unlike stemming. However, sometimes the resulting word is not the stem . Additionally, the POS tag can affect the result.
# </p>

# <codecell>

from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()
print lem.lemmatize('dog')
print lem.lemmatize('dogging')
print lem.lemmatize('dogging',pos='v')

# <codecell>

print porter.stem('believes')
print lem.lemmatize('believes')

