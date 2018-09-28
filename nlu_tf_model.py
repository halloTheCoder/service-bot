from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

import logging
import json
import os

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'service_nlu')
	
def run_nlu(file):
	read = 'w'
	if os.path.exists(file):
		read = 'a'
		added_texts = [x[:-1] for x in open(file, read).readlines()]
	else:
		added_texts = []

	f = open(file, read)

	interpreter = Interpreter.load('./models/nlu_tf/default/service_nlu')

	data = {"rasa_nlu_data": {"common_examples": [] } }
	
	while True:
		text = input('Enter text (Press \'q\' to continue) :: \n')
		if text == 'q':
			break
		nlu = interpreter.parse(text)
		# print(interpreter.parse(text))
		intent = nlu['intent']['name']
		entity = [{k:v for k, v in entity.items() if k in ['start', 'end', 'value', 'entity']} for entity in nlu['entities']]

		print(intent)
		print(entity)

		# if text not in added_texts:
		f.write(text + '\n')
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