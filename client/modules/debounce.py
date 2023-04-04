import machine

def Debounce(wait):
    """ Decorator that will postpone a functions
        execution until after wait seconds
        have elapsed since the last time it was invoked. """
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)
            try:
                debounced.t.cancel()
            except(AttributeError):
                pass
            debounced.t = machine.Timer(wait, call_it)
            debounced.t.start()
        return debounced
    return decorator

@Debounce(4)
def Test():
    print('did it')
    
Test()