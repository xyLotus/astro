import functools
import inspect


class TypeSpecError(Exception):
    """ The error of the typespec function wrapper
    being raised in the @function wrapper inside of
    @function typespec => inner_function. """
    pass

def _const_type_check(const_type: type, zipped: list):
    arg_count = 0

    print(zipped)
    for x in zipped:
        arg_count += 1
        print(x[0], ' | ', const_type)
        if x[0] != const_type:
            err_txt = f'\nArgument\'s {arg_count} type ({x[0]}) doesn\'t match ({const_type})'                    
            raise TypeSpecError(err_txt)

def _type_check(zipable: list):
    arg_count = 0

    for x in zip(zipable[0], zipable[1]):
        arg_count += 1
        if x[0] != type(x[1]):
            err_txt = f'\nArgument\'s {arg_count} type ({x[0]}) doesn\'t match ({type(x[1])})'                    
            raise TypeSpecError(err_txt)


def typespec(const_type = None, *argtypes, **kwtypes):
    """ This function wrapper accepts an unlimited amount
    of types being passed and checks if the types match  """
    def inner_function(_any):
        @functools.wraps(_any)

        def wrapper(*args, **kwargs):
            if const_type != None:
                _const_type_check(const_type, zip(argtypes, args))
                _const_type_check(const_type, zip(kwtypes, kwargs))
            else:
                _type_check([argtypes, args])
                _type_check([kwtypes, kwargs])

            _any(*args, **kwargs)

        return wrapper
    return inner_function


@typespec(int, int, int)
class Sample:
    def __init__(self, *args):
        self.args = args

sample = Sample("", 2, 2, "x", 2, 2)