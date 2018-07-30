from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
# agent = Agent.load('models/dialogue',interpreter='./models/current/nlu')
# agent.handle_channel(ConsoleInputChannel())
#

from rasa_core.interpreter import RasaNLUInterpreter

def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("./models/current/nlu")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
    run()