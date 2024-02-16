from datetime import datetime, timezone , date, time
def decorator_function(fn):
    def wrapper_function(*args, **kwargs):
        #Some actions before execution original_fn
        print(f"Executed before at {datetime.now().strftime('%d/%m/%Y')}")
        result = fn(*args, **kwargs)
        print("Executet after function")
        return result

    return wrapper_function

@decorator_function
def my_function(*args, **kwargs):
    print("This is my function!")
    return args, kwargs

print(my_function(100,50,1000))


# Example logging

def log_function_call(origin_fn):
    def wraper(*args, **kwargs):
        print(f"The function name: {origin_fn.__name__}")
        print(f"The functions arguments: {args}, {kwargs}")
        result = origin_fn(*args, **kwargs)
        print(f"The function result: {result}")
        return result

    return wraper
@log_function_call
def mult(a, b):
    return a * b


print(mult(5, 2 ))



# Example check_user_auth
def is_user_autentificated():
    return True
def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_autentificated():
            print("User is autentificated!")
            return fn(*args, **kwargs)
        else:
            raise Exception("User is NOT autentificated!")

    return wrapper

@check_user_auth
def some_function():
    print("Results of some sensitive task")

try:
    some_function()
except Exception as e:
    print(e)