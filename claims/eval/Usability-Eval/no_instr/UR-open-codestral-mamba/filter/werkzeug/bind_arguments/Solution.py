from werkzeug.datastructures import ImmutableMultiDict

def my_function(arg1, arg2, arg3):
    request_params = ImmutableMultiDict([
        ('arg1', arg1),
        ('arg2', arg2),
        ('arg3', arg3)
    ])

    return request_params

result = my_function('value1', 'value2', 'value3')
print(dict(result))
