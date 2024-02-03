user_name = "Bazhen"
def greeting(greet):
    return lambda name: f"{greet} {name}!" #key (lambda) => 'parameters'(name) => : => 'expression'(f"{greet} {name}!")

morning_greeting = greeting('Good Morning') #Good Morning

print(morning_greeting(user_name)) #Good Morning Bazhen!

evening_greeting = greeting("Good Evening") #Good Morning

print(evening_greeting(user_name)) #Good Morning Bazhen!