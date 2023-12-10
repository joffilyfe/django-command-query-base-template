from typing import Optional, Iterable


class BaseAuthorizer:
    """BaseAuthorizer defines how child classes should behavior
    when called by EntryPoints"""

    def __init__(self, entry_point: "BaseEntryPoint") -> None:
        self.entry_point = entry_point

    def check(self) -> None:
        raise NotImplementedError


class BaseAction:
    """BaseAction class defines how action classes behave"""

    def __call__(self):
        raise NotImplementedError


class AuthorizerError(Exception):
    ...


class BaseEntryPoint:
    """Base class that defines how authorizers and actions are called.

    Every unit that use entry point pattern should inherent from here."""

    authorizers: Iterable[BaseAuthorizer] = []
    action: Optional[BaseAction] = None

    def execute(self):
        self.run_authorizers()

        if hasattr(self, "action"):
            self.action()

        if hasattr(self, "form"):
            ...

    def run_authorizers(self):
        for authorizer in self.authorizers:
            authorizer(self).check()


def entry_point(cls):
    """Decorates entry points classes"""

    class Base(cls, BaseEntryPoint):
        ...

    return Base


class Meta(type):
    def __getattribute__(cls, name: str):
        if name == "objects" and cls.MODEL:
            return getattr(cls.MODEL, name)

        return super().__getattribute__(name)


class BaseQuery(metaclass=Meta):
    @classmethod
    def by_pk(cls, pk: int):
        return cls.MODEL.objects.get(pk=pk)


def query(cls):
    """Alternative decorator that injects BaseQuery Meta Class"""

    class Base(cls, BaseQuery):
        ...

    return Base
