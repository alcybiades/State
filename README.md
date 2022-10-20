# State

This is a pedagogical exercise to construct the foundations of math (arithmetic) from nothing more than a basic notion of encapsulation (i.e. a Python class which can either hold nothing or just one object which is itself of the same class). No loops, no numbers, no foundational types except for `State`. If statements are used, but only to discern whether something is `None`.

Philosophically, the motivation here is to more clearly frame the foundations of mathematics as 'difference within the same' - the 'difference' being the capacity for a `State` object to contain either another `State` object (Something) or `None` (Nothing), and the 'within' being the recursive, hierarchical nature of classes in object oriented languages.
