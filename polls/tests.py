import datetime

from django.test import TestCase
from django.utils import timezone
from .queries import QuestionQueries
from .models import Question


class QuestionQueriesTests(TestCase):
    def test_published_recently_returns_todays_question(self):
        Question(pub_date=timezone.now()).save()

        self.assertQuerySetEqual(
            QuestionQueries.published_recently(), QuestionQueries.objects.all()
        )

    def test_published_recently_does_not_return_last_week_question(self):
        time = timezone.now() - datetime.timedelta(days=7)
        Question(pub_date=time).save()

        self.assertQuerySetEqual(QuestionQueries.published_recently(), [])
