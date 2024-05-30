def intercept_return(func):

    def _intercept_return(*args):
        ret = func(*args)
        return "Intercepted: " + ret + ", returning Bye!"

    return _intercept_return


@intercept_return
def greet():
    return "Hello, world!"


class A:

    @intercept_return
    def greet(self):
        return "Hello, world!"
        

def logger(func):

    def _logger(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))
            
        return result

    return _logger

        
@logger
def summator(numlist):
    return sum(numlist)


def summator2(numlist):
    return sum(numlist)


summator2 = logger(summator2)
