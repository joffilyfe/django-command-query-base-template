from core import BaseEntryPoint, BaseAction
from polls.queries import ChoiceQueries
from django.core.exceptions import ObjectDoesNotExist


class RegisterVote(BaseEntryPoint):
    def __init__(self, choice_id):
        self.action = Action(choice_id)


class Action(BaseAction):
    def __init__(self, choice_id):
        self.choice_id = choice_id

    def __call__(self):
        try:
            choice = ChoiceQueries.by_pk(self.choice_id)
            choice.votes += 1
            choice.save()
        except ObjectDoesNotExist:
            print(f"Could not find choice#{self.choice_id}")
            return False
