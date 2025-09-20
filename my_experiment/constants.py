from otree.api import BaseConstants

class Constants(BaseConstants):
    name_in_url = 'my_experiment'
    players_per_group = None  # 個人単位の実験
    num_rounds = 30  # 問題数
    num_questions = 30

    # サンプルの問題文リスト
    QUESTIONS = [
        "問題1: 1+1は？",
        "問題2: 3×3は？",
        "問題3: Pythonはプログラミング言語か？",
        # …必要に応じて30問まで追加
    ]
