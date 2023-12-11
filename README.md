# Experiment Using Command & QueryObject Patterns

This weekend, I conducted an experiment to explore the behavior of the framework structure when employing command, units, and query-object patterns in unison.

As far as I am aware, these patterns are not widely embraced within the Django community but are quite prevalent in the Rails world.

## Command Structure

I chose to implement the `<app>/units/<unit_name>/__init__.py` structure to investigate how commands could be defined, imported, and utilized across different layers.

For instance, consider the `CreateQuestion` command, which resides at the following path: `polls/units/create_question/__init__.py`. To use it, you may import it from the `polls` app and then invoke it as `CreateQuestion(params).execute()`.

The advantage of this pattern is to centralize the business logic of creating a `Question` within a module that comprehensively understands its. The `EntryPoint` structure allows us to define authorizers that verify if, given specific input, the unit can invoke its action. Also, checks if params have correct data.

This example does not currently utilize Django Signals, but it could be incorporated later. _[to be added later]_.

## Query-Object
..
