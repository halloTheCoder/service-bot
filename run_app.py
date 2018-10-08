from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig
from rasa_core import constants

from flask import Flask
from gevent.pywsgi import WSGIServer


nlu_interpreter = RasaNLUInterpreter('./models/nlu_tf/default/service_nlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxb-446873191671-445226503153-NDkcQJudWyXwTrxiLn1WT4dj') #your bot user authentication token
					 

class CustomAgent(Agent):
	def __init__(self):
		super(CustomAgent, self).__init__()

	def handle_channels(channels, http_port=constants.DEFAULT_SERVER_PORT, serve_forever=True):
		# type: (List[InputChannel], int, bool) -> WSGIServer
		"""Start a webserver attaching the input channels and handling msgs.
		If ``serve_forever`` is set to ``True``, this call will be blocking.
		Otherwise the webserver will be started, and the method will
		return afterwards."""
		from flask import Flask

		application = Flask(__name__)
		rasa_core.channels.channel.register(channels,
											app,
											self.handle_message,
											route="/webhooks/")

		http_server = WSGIServer(('0.0.0.0', http_port), application)
		http_server.start()

		if serve_forever:
			http_server.serve_forever()
		return http_server

agent = CustomAgent()
agent.handle_channels([input_channel], 5004, serve_forever=True)
