Feature: Candy Wrapper is a "sticky" wrapper for any object, which adds syntax surgar

    This wrapper wraps any object, and give the ability
    to add attributes to the object like a dictionary,
    much in the same way that pandas dataframs work.

    from candy_wrapper.candy_wrapper import Wrapper
    foo = SomeClass()
    candy = Wrapper(foo)
    foo['bar'] = 42
    print(foo.bar) # prints 42
    setattr(foo,'hey',420)
    print(foo['hey']) # prints 420

  Background: foo = Wrapper('foo')
    Given foo = Wrapper('foo')

  Scenario: foo['bar'] = 42
    Given foo['bar'] = 42
     When foo.bar
     Then returns 42

  Scenario: setattr(foo,'hey',420)
    Given setattr(foo,'hey',420)
     When foo['hey']
     Then returns 420

  Scenario: foo()
       When foo()
       Then returns foo
  
  