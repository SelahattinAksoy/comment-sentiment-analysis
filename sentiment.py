import random
import nltk
import string
from nltk.corpus import stopwords
import product_comments

def read_txt_file():
    file1 = open('Data\pozitive.txt', 'r', encoding='utf8')
    Lines = file1.readlines()
    positive = [(sent, "pos") for sent in Lines]

    file2 = open('Data\\negative.txt', 'r', encoding='utf8')
    Line = file2.readlines()
    negative = [(sent, "neg") for sent in Line]

    return positive+negative
whole_sentence=read_txt_file() #[('Çaykur’u Liptonu diğerlerini geçer.\n', 'pos'), ('Çok güzel çayGüvenilir mağaza tavsiye ederim....\n', 'pos'),


def clean_punctuation(text):
    trans = str.maketrans("", "", string.punctuation)
    return text.translate(trans)

def split_sentence_to_word(doc):
  words=[]
  for (sent,sentiment) in doc:
    all_words=[clean_punctuation(e.lower()) for e in nltk.word_tokenize(sent) if len(e)>2 ]
    words.append((all_words,sentiment))
  return words

splited_sentence=split_sentence_to_word(whole_sentence) #[(['çaykur’u', 'liptonu', 'diğerlerini', 'geçer'], 'pos'), (['çok', 'güzel', 'çaygüvenilir', 'mağaza', 'tavsiye', 'ederim'], 'pos')



def all_words_infile(doc):
  all_words=[]
  for(word,sen) in doc:
    all_words.extend(word)
  return all_words;

def clean_stopwords(doc):
  nltk.download('stopwords')
  all_word=[]
  for i in doc:
    if i  not in stopwords.words("turkish"):
      all_word.append(i)
  return all_word


all_words=clean_stopwords(all_words_infile(splited_sentence)) #['çaykur’u', 'liptonu', 'diğerlerini', 'geçer', 'güzel',...

def freq_dist(doc):
  fre=nltk.FreqDist(doc);
  return fre.keys()


all_words_uniq=freq_dist(all_words)


def create_feature(data):
  data=set(data)
  feature={}
  for i in all_words_uniq:
    feature[i]=(i in data)
  return feature


random.shuffle(splited_sentence)


def classify_text(text):

    return (classifier.classify(text))

def show_accurcy(classify,testing_set):
    print("Accurcy :",nltk.classify.accuracy(classifier,testing_set))


def train_Naive_bayes(train_set):

    return nltk.NaiveBayesClassifier.train(train_set)

def read_comment_from_n11():
    product_comments.read_n11_comment()

def classify_comments():
    print("Classifyed Comments")
    file1 = open('Data\comments.txt', 'r', encoding='utf8')
    Lines = file1.readlines()
    positive = [(classify_text(create_feature(sent.split())), "(" + sent + ")") for sent in Lines]

    for i in positive:
        print(i)

def read_comment_txt():
    file1 = open('Data\comments.txt', 'r', encoding='utf8')
    Lines = file1.readlines()
    print(Lines)

def read_links_txt():
    file1 = open('Data\links.txt', 'r', encoding='utf8')
    Lines = file1.readlines()
    print(Lines)
feature_setes=[(create_feature(rev),sen)  for (rev,sen) in splited_sentence]
training_set=feature_setes[:49]
testing_set=feature_setes[49:]
classifier=train_Naive_bayes(training_set)


show_accurcy(classifier,testing_set) #showing accury by show_accurcy function
classify_comments()
