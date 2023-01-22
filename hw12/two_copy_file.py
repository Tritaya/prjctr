content = '''Тому що ніколи тебе не вирвеш,
ніколи не забереш,
тому що вся твоя свобода
складається з меж,
тому що в тебе немає
жодного вантажу,
тому що ти ніколи не слухаєш,
оскільки знаєш і так,
що я скажу,'''


print(content)

with open('lower.txt', 'w', encoding='utf-8-sig') as f, \
     open('upper.txt', 'w', encoding='utf-8-sig') as u:
     f.write(content)
     u.write(content.upper())