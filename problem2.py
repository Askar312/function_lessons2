text = input("Введите имя:")
def name(text):
    count = 0
    for i in text:
        count += 1
    return count
print("В вашем имемни столько букв:", name(text))