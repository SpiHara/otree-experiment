from otree.api import *

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
    correct_answers = ['A','B','C']  # 仮の正解リスト

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    has_competitor = models.BooleanField(initial=False)
    response_time = models.FloatField()
    answer = models.StringField(
        choices=['A','B','C','D'],
        label='あなたの回答'
    )
    is_correct = models.BooleanField(initial=False)
