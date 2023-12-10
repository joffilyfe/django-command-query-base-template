from unittest import mock
from django.test import TestCase
from . import BaseAction, BaseAuthorizer, BaseEntryPoint


class BaseActionTests(TestCase):
    def test_implements_call(self):
        self.assertTrue(callable(BaseAction()))


class BaseAuthorizerTests(TestCase):
    def setUp(self):
        self.authorizer = BaseAuthorizer(entry_point=mock.Mock())

    def test_implements_check(self):
        self.assertTrue(callable(self.authorizer.check))


class BaseEntryPointTests(TestCase):
    def setUp(self):
        self.entry_point = BaseEntryPoint()
        self.authorizers = [mock.Mock(BaseAuthorizer), mock.Mock(BaseAuthorizer)]
        self.action = mock.MagicMock()
        self.entry_point.authorizers = self.authorizers
        self.entry_point.action = self.action
        self.entry_point.execute()

    def test_calls_action_class(self):
        self.action.assert_called()

    def test_iterates_over_authorizers_and_call_them(self):
        for authorizer in self.authorizers:
            authorizer(self.entry_point).check.assert_called()
