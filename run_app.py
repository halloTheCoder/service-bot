from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core import constants
from rasa_core.channels import channel, slack

from rasa_core.utils import EndpointConfig

from rasa_core.policies.ensemble import SimplePolicyEnsemble, PolicyEnsemble
from rasa_core.domain import Domain, check_domain_sanity


import yaml

from flask import Flask
from gevent.pywsgi import WSGIServer


nlu_interpreter = RasaNLUInterpreter('./models/nlu_tf/default/service_nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

class CustomAgent(Agent):
	# def __init__(self):
	# 	super(CustomAgent, self).__init__()

	def handle_channels(self, channels, http_port=constants.DEFAULT_SERVER_PORT, serve_forever=True):
		# type: (List[InputChannel], int, bool) -> WSGIServer
		"""Start a webserver attaching the input channels and handling msgs.
		If ``serve_forever`` is set to ``True``, this call will be blocking.
		Otherwise the webserver will be started, and the method will
		return afterwards."""
		from flask import Flask

		application = Flask(__name__)
		channel.register(channels,
						 application,
						 super(CustomAgent, self).handle_message,
						 route="/webhooks/")

		http_server = WSGIServer(('0.0.0.0', http_port), application)
		http_server.start()

		if serve_forever:
			http_server.serve_forever()
		return http_server


agent = CustomAgent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)					 

print('\nPrinting ...')
print(agent.__class__.__name__)
print()

input_channel = slack.SlackInput('xoxb-446873191671-445226503153-NDkcQJudWyXwTrxiLn1WT4dj') #your bot user authentication token
agent.handle_channels([input_channel], 5004)
