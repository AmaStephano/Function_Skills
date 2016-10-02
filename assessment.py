
"""
Assessment Tests

PART ONE:

    >>> calc_total('CA', 5.00)
    '$5.35'

    >>> calc_total('IL', 6.00)
    '$6.30'

PART TWO:

    >>> is_berry('apple')
    False

    >>> is_berry('cherry')
    True

    >>> shipping_cost('strawberry')
    0

    >>> shipping_cost('pineapple')
    5

    >>> is_hometown('Saint Charles')
    True

    >>> is_hometown('San Francisco')
    False

    >>> full_name('Amanda', 'Stephano')
    'Amanda Stephano'

    >>> hometown_greeting('San Francisco', 'Amanda', 'Stephano')
    Hi, Amanda Stephano, where are you from?

    >>> hometown_greeting('Saint Charles', 'Amanda', 'Stephano')
    Hi, Amanda Stephano, we're from the same place!

    >>> addfive = increment(5)
    >>> addfive
    10

    >>> addfive = increment(20)
    >>> addfive
    40

    >>> append_to_list(5, [1, 2, 3, 4])
    [1, 2, 3, 4, 5]
"""

# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def calc_total(state, cost, tax=.05):
    if state == "CA":
        tax = .07
    total = '$' + '{0:.2f}'.format(cost + (cost * tax))
    return total



#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def is_berry(fruit):
    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False


def shipping_cost(fruit):
    if is_berry(fruit):
        return 0
    elif not is_berry(fruit):
        return 5


def is_hometown(town):
    if town == "Saint Charles":
        return True
    else:
        return False


def full_name(first_name, last_name):
    name = "%s %s" % (first_name, last_name)
    return name


def hometown_greeting(home_town, first_name, last_name):
    name = full_name(first_name, last_name)
    if is_hometown(home_town):
        print "Hi, %s, we're from the same place!" % (name)
    else:
        print "Hi, %s, where are you from?" % (name)



#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def increment(x=1):
    def add(y):
        sum = x + y
        return sum
    return (add(x))

addfive = increment(5)
addfive = increment(20)


def append_to_list(num, list_of_nums):
    list_of_nums.append(num)
    return list_of_nums




#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
