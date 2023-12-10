import datetime
from core import BaseEntryPoint, BaseAuthorizer, BaseAction, AuthorizerError
from polls.models import Question
from django.core.exceptions import ValidationError


class UserAuthorizer(BaseAuthorizer):
    def check(self):
        """Check if the user/employee/person has permission to perform
        this action"""

        if self.entry_point.user["name"] == "Joffily":
            return None

        raise AuthorizerError("User not authorized")


class CreateQuestion(BaseEntryPoint):
    def __init__(self, text: str, pub_date: datetime.datetime):
        self.action = Action(text, pub_date)


class Action(BaseAction):
    def __init__(self, text: str, pub_date: datetime.datetime):
        self.text = text
        self.pub_date = pub_date

    def __call__(self):
        question = Question(question_text=self.text, pub_date=self.pub_date)

        try:
            question.full_clean()
            question.save()
        except ValidationError:
            print("Validation Error")
            return False
