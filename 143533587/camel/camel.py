name = input("camelCase: ")
snake = []
for word in name:
    if word == word.upper():
        snake.append("_")
    snake.append(word.lower())
print("snake_case:",*snake, sep = "")