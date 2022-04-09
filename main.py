import random
import re

def generateModel(filename):
  model = {} 
  for line in open(filename):
    # Swap all lowercase characters not in the Regular Expression for a space, 
    # then split the line at every chunk of spaces into a list.
    words = re.sub('[^a-z\'\s]', ' ', line.lower()).split()
    lastWord = None
    for word in words:
      if word not in model:
        model[word] = {}
      if lastWord:
        if word not in model[lastWord]:
          model[lastWord][word] = 0
        model[lastWord][word] += 1
      lastWord = word
  for word in model:
    totalNextWords = sum(model[word].values())
    for nextWord in model[word]:
      model[word][nextWord] /= totalNextWords
  return model

# Return a key at random from the list of model keys,
# where a key is a unique word in the corpus.
def getRandomWord(model):
  return random.choice(list(model.keys()))

def getRandomNextWord(model, word):
  targetAngle = random.random()
  angle = 0
  for nextWord in model[word]:
    angle = angle + model[word][nextWord]
    if angle >= targetAngle:
      return nextWord
  return None

def generateWords(model, numWords):
  word = getRandomWord(model)
  generatedText = word
  while numWords > 0:
    nextWord = getRandomNextWord(model, word)
    if nextWord:
      generatedText = generatedText + " " + nextWord
      numWords = numWords - 1
      word = nextWord
    else:
      generatedText = generatedText + "."
      word = getRandomWord(model)
  print(generatedText.capitalize() + ".")

BooksModel = generateModel('Books.txt')
generateWords(BooksModel, 20)
