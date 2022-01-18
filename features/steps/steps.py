from behave import *
from candy.candy_wrapper import Wrapper
from pysimplelog import Logger

logger = Logger('behave')
logger.set_log_file_basename(__name__)
logger.set_minimum_level(logger.logLevels['debug'])


@given(u'foo = Wrapper(\'foo\')')
def step_impl(context):
    context.foo = Wrapper('foo')

@given(u'foo[\'bar\'] = 42')
def step_impl(context):
    context.foo['bar'] = 42


@when(u'foo.bar')
def step_impl(context):
    context.returns = context.foo.bar

@then(u'returns 42')
def step_impl(context):
    assert context.returns() == 42

@given(u'setattr(foo,\'hey\',420)')
def step_impl(context):
    setattr(context.foo, 'hey', 420)

@when(u'foo[\'hey\']')
def step_impl(context):
    logger.debug(context.foo['hey'])
    context.returns = context.foo['hey']


@then(u'returns 420')
def step_impl(context):
    logger.debug(context.returns)
    assert context.returns() == 420

@when(u'foo()')
def step_impl(context):
    context.returns = context.foo()

@then(u'returns foo')
def step_impl(context):
    assert context.returns == 'foo'