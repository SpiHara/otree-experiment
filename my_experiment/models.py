from otree.api import (
    BaseConstants, BaseSubsession, BaseGroup, BasePlayer, models
)

class Constants(BaseConstants):
    name_in_url = 'quiz'
    players_per_group = None
    num_rounds = 30
    question_list = [
        "問題1: 例題1",
        "問題2: 例題2",
        "問題3: 例題3",
        # …30問まで
    ]
    correct_answers = ['A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D','A','B','C','D','A','B']  # 30個の正解

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    has_competitor = models.BooleanField(initial=False)
    start_time = models.FloatField(initial=0.0)  # 追加
    response_time = models.FloatField()
    answer = models.StringField(
        choices=['A','B','C','D'],
        label='あなたの回答'
    )
    is_correct = models.BooleanField(initial=False)
