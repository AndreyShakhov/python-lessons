with open('dataset_3363_3.txt', 'r') as inf:
    input_text = ''
    for line in inf:
        input_text += line.strip()
        print('hello')
text_list = input_text.split()
set_words_text = set(text_list)
quantity_words = {}
quantity = 0
prevolution_quantity = 0
for word in set_words_text:
    quantity = text_list.count(word)
    if quantity > prevolution_quantity:
        quantity_words.clear()
        quantity_words[word] = quantity
        prevolution_quantity = quantity

print(quantity_words)