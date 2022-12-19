def calcSum(n1, n2):
    return n1 + n2


g = 0
def increment():
    """
    this increments the variable g over multiple calls, it's basically a fancy
    counter
    This is written in a comment btw. and can be called under __doc__
    """
    # sets g as global variable across modules
    global g
    g += 1

    # returns new g as function output
    return g
