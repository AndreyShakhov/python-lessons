number_list = '0123456789'
with open('text.txt', 'r') as inf:
    string_input = inf.readline().strip()
multiplier = ''
string_input_element = ''
decrypted_string_revers = ''
string_input_reverse = string_input[::-1]
for i in range(len(string_input_reverse)):
    l = string_input_reverse[i]
    if string_input_reverse[i] not in number_list:
        if multiplier == '':
            multiplier = '1'
       string_input_element = string_input_reverse[i] * int(multiplier[::-1])
       decrypted_string_revers += string_input_element
       multiplier = ''
    else:
        multiplier += string_input_reverse[i]
print(decrypted_string_revers[::-1])




