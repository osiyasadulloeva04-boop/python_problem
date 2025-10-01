#task 2
colors = [
    {"Green": "#008000"},
    {"Black": "#000000"},
    {"Blue": "#0000FF"},
    {"Green": "#008000"}
]

result = []
for color in colors:
    
    if color not in result:
        result.append(color)


print(result)