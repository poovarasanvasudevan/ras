from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_nlu import config
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.train import do_train
from rasa_nlu.components import ComponentBuilder

if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    builder = ComponentBuilder(
        use_cache=False
    )
    do_train(
        cfg=config.load("./nlu_config.yml"),
        data='data/nlu_data.md',
        path='models',
        fixed_model_name="nlu",
        project='current',
        component_builder=builder
    )

    # train_dialogue_model(
    #     domain_file='domain.yml',
    #     stories_file='data/stories.md',
    #     output_path='./models/dialogue/',
    #     max_history=10,
    #     nlu_model_path='./data/nlu_data.md',
    #     kwargs={
    #         "fixed_model_name": "current",
    #         "epochs":500,
    #         "max_training_samples":300
    #     }
    #
    # )
    # builder = ComponentBuilder(
    #     use_cache=False
    # )  # will cache components between pipelines (where possible)
    #
    # training_data = load_data('./models/dialogue/')
    # trainer = Trainer(config.load("./nlu_config.yml"), builder)
    # trainer.train(training_data)
    # model_directory = trainer.persist('./models/nlu/', fixed_model_name="current")
