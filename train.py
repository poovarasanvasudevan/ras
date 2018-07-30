from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.train import train_dialogue_model

from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.agent import Agent

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    training_data_file = './data/stories.md'
    model_path = './models/dialogue'

    fallback = FallbackPolicy(
        fallback_action_name="unknown",
        core_threshold=0.3,
        nlu_threshold=0.3)

    agent = Agent("domain.yml",
                  policies=[MemoizationPolicy(max_history=10), KerasPolicy(), fallback])
    training_data = agent.load_data(training_data_file)

    agent.train(
        training_data,
        augmentation_factor=50,
        # max_history=10,
        epochs=500,
        batch_size=10,
        validation_split=0.2,
        fixed_model_name="current",
        max_training_samples=300
    )

    agent.persist(model_path)

    # train_dialogue_model(
    #     domain_file='domain.yml',
    #     stories_file=training_data_file,
    #     output_path=model_path,
    #     max_history=10,
    #     nlu_model_path='./data/nlu_data.md',
    #     kwargs={
    #         "fixed_model_name": "current",
    #         "epochs": 500,
    #         "batch_size": 100,
    #         "validation_split": 0.2,
    #         "max_training_samples": 300
    #     }
    # )
