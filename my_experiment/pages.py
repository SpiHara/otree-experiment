from ._builtin import Page, WaitPage
from .models import Constants, Player, Group
import random, time

# 導入ページ
class Introduction(Page):
    def before_next_page(player: Player, timeout_happened):
        # 50%の確率で競争者あり
        player.has_competitor = random.choice([True, False])

# 問題ページ
class Quiz(Page):
    form_model = 'player'
    form_fields = ['answer']
    
    def is_displayed(player: Player):
        import time
        player.start_time = time.time()  # ページ表示時に記録
        return True

    def vars_for_template(player: Player):
        q_index = player.round_number - 1
        return {
            'question_text': Constants.question_list[q_index],
            'correct_answer': Constants.correct_answers[q_index],
            'question_number': player.round_number,
            'total_questions': Constants.num_rounds,
            'competitor': player.has_competitor
        }

    def before_next_page(player: Player, timeout_happened):
        import time
        player.response_time = time.time() - player.start_time  # 正確な計算
        player.is_correct = player.answer == Constants.correct_answers[player.round_number-1]

# WaitPage（競争者がいる場合に同期）
class WaitForCompetitors(WaitPage):
    wait_for_all_groups = True  # 全員揃うまで待機
    def after_all_players_arrive(group: Group):
        pass

# 結果ページ
class Results(Page):
    def vars_for_template(player: Player):
        return {
            'is_correct': player.is_correct,
            'answer': player.answer,
            'correct_answer': Constants.correct_answers[player.round_number-1],
            'competitor': player.has_competitor
        }

page_sequence = [Introduction, WaitForCompetitors, Quiz, Results]

