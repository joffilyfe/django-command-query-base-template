import datetime
from django.utils import timezone
from polls import models
from core import query


@query
class QuestionQueries:
    MODEL = models.Question

    @classmethod
    def published_recently(cls):
        return cls.MODEL.objects.filter(
            pub_date__gte=timezone.now() - datetime.timedelta(days=1)
        )


@query
class ChoiceQueries:
    MODEL = models.Choice
