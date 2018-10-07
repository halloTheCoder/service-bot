import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.training import online
from rasa_core.utils import EndpointConfig

from policy import BotPolicy

logger = logging.getLogger(__name__)


def run_weather_online(interpreter,
                       domain_file = "domain.yml",
                       training_data_file = 'stories.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")						  
    agent = Agent(domain_file,
                  policies = [MemoizationPolicy(max_history = 4), BotPolicy()],
                  interpreter = interpreter,
				          action_endpoint = action_endpoint)
    				  
    data = agent.load_data(training_data_file)
    agent.train(data,
				batch_size = 32,
				epochs = 70,
				validation_split = 0.2)				   
    online.run_online_learning(agent)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu_tf/default/service_nlu')
    run_weather_online(nlu_interpreter)
