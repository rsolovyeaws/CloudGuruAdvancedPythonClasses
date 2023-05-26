## (instance).__dict__  
get the dictionary representation of an object
that includes all of the attributes of the object

## dir(instance) / dir(class)
See the list of all of the attributes and functions on an object

## isinstance(instance, class) 
Determine if the object is an instance of an object.
Subclass objects are instances of the super class.

## help(instance) / help(class)
See help information for a type if it exists

## Data model:
    - override dunder methods (__eq__, __ne__... etc)


## Class methods  (Decorated: @classmethod)
     @classmethod
     def name(cls, ...):
        can only access class data
    
    cls can be used to return instantiated class
        return cls(...)

## Static methods (Decorated: @staticmethod)
    Just functions, don't access any class or instance data by default

## Composition 
    Separate responsibilities into objects...
    Car <- Tire
    Used to create layers of abstraction and separate responsibilities 

## Inheritance
    Used to create more specific versions of a broader type. 
    Allows for adding and modifying functionality of existing types by creating a new type

## Polymorphism 
    Since we cannot enforce what is passed to the object
    if passed object has expected behavior it is considered to be an expected object

## Hiding attributes
    _x - can be accessed via (instance)._x (single underscore means it should not be accessed)
    __x = can be accessed  via (instance._(class)__x) 

## Property Decorator (@property)
    Used to fine tune setting, getting and deleting of the class attributes
    _x = ...

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        #some logic
        self._x = value
    
    @x.deleter
    def x(self):
        del self._x

## Variadic functions
    Accept infinite number of arguments
        - *remainder is a tuple
    def function(first_arg, *remainder): 
        print(first_arg)
        for arg in *remainder
            print(arg)
        - **kwargs is a dictionary
    
    def function(first_arg, **kwargs):
        print(first_arg)

## Decorator
    A function that returns another function
    Order of operations upwards:
    3 @dec1
    2 @dec2
    1 def func()

## Class-based decorator
    Decorates function as a class
    Requires __call__ implementation
    Decorated function can be treated as a class afterwards

## Decorating Class
    You can decorate a class with a function
    Class callable returns an instance of the class so the decorator will return that instance
    Essentially decorating the class constructor
    In the decorator function:
        - can decorate class 
        - can decorate instance

## Comparison
    == is by value
    is is by mem loc
    id(var) - mem loc

## Copying
    mutable types(Dictionary, List, Custom Object) passed to the function will be changed by the function
        use copy.copy() or copy.deepcopy() 

    list slicing also makes a copy
        my_other_list = my_list[:]

    
## Abstract base classes 
    introduce virtual subclasses:
        - do not inherit from the class, but are recognized by
            isinstance() and issubclass() 

    from abc import ABC, abstractmethod, abstractclassmethod, abstractstaticmethod

    enforce polymorphism
    not exactly an interface, because it can have concrete implementation of methods

## Metaprogramming
    code that creates and/or changes code
    'type' class is default metaclass for all classes in Python
    custom metaclasses - customizes how class is made by defining new metaclass

    Foo = type("Foo", (base_classes), {attributes} )

## Exception 
    Exceptions are normal classes
        have custom parameters
    Access traceback as a string while still handling exception:
        import traceback
        ...
        try:
        except ZeroDivisionError as err:
            tb = traceback.format_tb(err.__traceback__)
            print(tb)
    
    Exceptions can be implicitly chained: 
        During handling of the above exception, another exception occurred:
    or Explicitly chained:
        The above exception was the direct cause of the following exception:

    

     