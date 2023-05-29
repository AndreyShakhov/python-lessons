famous_words = set()
unknown_words = set()

for _ in range(int(input())): # формируем словарь известных слов
    famous_words.add(input().strip().lower())

for _ in range(int(input())): # формируем список слов для проверки
    for word in input().strip().lower().split():
        if word not in famous_words: # слова отсутствующие в словаре известных слов - добавляем в словарь неизвестных
            unknown_words.add(word)

for word in unknown_words:
    print(word)