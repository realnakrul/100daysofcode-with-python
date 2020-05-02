from functools import wraps


def make_html(element):
    def wrap(func):
        def wrapped_f(*args):
            elem_open = '<{}>'.format(element)
            elem_close = '</{}>'.format(element)
            return elem_open + func(*args) + elem_close
        return wrapped_f
    return wrap


@make_html('p')
@make_html('p')
def get_text(text='I code with PyBites'):
    return text


print(get_text())



