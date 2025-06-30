import os

# Папка, где будут создаваться файлы (укажи свою папку с репо!)
output_dir = './'  # текущая папка, где лежит скрипт

# Читаем данные
with open('titles.txt', encoding='utf-8') as f:
    titles = [line.strip() for line in f if line.strip()]

with open('links.txt', encoding='utf-8') as f:
    links = [line.strip() for line in f if line.strip()]

if len(titles) != len(links):
    print("Ошибка: количество заголовков и ссылок не совпадает")
    exit(1)

template = '''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <title>{title}</title>
</head>
<body>
  <h1>{title}</h1>
  <p>Подписывайтесь на наш Telegram-канал:</p>
  <a href="{link}" target="_blank">{link}</a>
</body>
</html>
'''

for i, (title, link) in enumerate(zip(titles, links), start=1):
    safe_title = f'channel_{i}.html'
    content = template.format(title=title, link=link)
    path = os.path.join(output_dir, safe_title)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Создан файл: {safe_title}')
