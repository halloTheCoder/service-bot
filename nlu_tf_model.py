from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

import logging
import json
import os
import re

import spacy.tokenizer
from spacy.lemmatizer import Lemmatizer

nlp = spacy.load('en')
tokenizer = spacy.tokenizer.Tokenizer(nlp.vocab)

def preprocess_text(text, remove_stopwords=True):
    global tokenizer
    text = text.lower().strip()
    tokens = tokenizer(text)
    text = [x.text for x in tokens]
    
    # Optionally, remove stop words
    if remove_stopwords:
#         stops = set(stopwords.words("english"))
        own_stopword = ['the','on','a','an','it','be','has','some','my','me', 'i']
        stops = own_stopword
        text = [w for w in text if not w in stops]
    
    text = " ".join(text)
    
    if text[-1] in ['.','?']:
        text = text[:-1] + ' ' + text[-1]
        
    # Clean the text
    text = re.sub(r"[^A-Za-z0-9^,:!.\/'+=@-]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r" n ", " and ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "cannot ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    # text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ", text)
    # text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    # text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    # text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)

    text = re.sub(' +', ' ', text)
    
    return text

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'service_nlu')
	
def run_nlu(file):
	# read = 'w'
	# if os.path.exists(file):
	# 	read = 'a'
	# 	added_texts = [x[:-1] for x in open(file, read).readlines()]
	# else:
	# 	added_texts = []

	# f = open(file, read)

	interpreter = Interpreter.load('./models/nlu_tf/default/service_nlu')

	data = {"rasa_nlu_data": {"common_examples": [] } }
	
	while True:
		text = input('Enter text (Press \'q\' to continue) :: \n')
		if text == 'q':
			break

		text = preprocess_text(text)
		print(text)

		nlu = interpreter.parse(text)
		# print(interpreter.parse(text))
		intent = nlu['intent']['name']
		entity = [{k:v for k, v in entity.items() if k in ['start', 'end', 'value', 'entity']} for entity in nlu['entities']]

		print(intent)
		print(entity)

		# if text not in added_texts:
		# f.write(text + '\n')
		data['rasa_nlu_data']['common_examples'].append({"text" : text, 
														 "intent" : intent, 
														 "entities" : entity})
	
	read = 'w'
	if os.path.exists('test_tf.json'):
		read = 'a'
	with open('test_tf.json', read) as f:
		json.dump(data, f, indent = 4)

	
if __name__ == '__main__':
	# train_nlu('./data/data.json', 'config_tensorflow.yml', './models/nlu_tf')
	run_nlu('all_texts_tf.txt')