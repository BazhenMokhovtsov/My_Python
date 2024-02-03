#creating a dict
button = {
    'width': 200,
    'text': 'Buy',
    'color': 'green'
}
#createing new dict and use ** to merger dict(botton) and dict(redbotton)
#value for key 'color' are changing from 'green' to 'red'
redbutton = {
    **button,
    'color': 'red',
}

#print(button)
#print(redbutton)

button_info = {
    'text': 'Buy',
}

button_style = {
    'color': 'gray',
    'width': 156,
    'height': 222,
}
#merger two dict with operator '|' .
new_button = button | button_info | button_style

#print(new_button)