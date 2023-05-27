with open('dataset_3363_4.txt', 'r+') as inf, open('itog.txt', 'w') as itog :
    input_spisok = ''
    list_element_input_spisok = []
    average_ball = 0
    abiturient_quantity = 0
    subject_one = 0
    subject_two = 0
    subject_three = 0
    for line in inf:
        input_spisok = line.strip()
        list_element_input_spisok = input_spisok.split(';')
        average_ball = (int(list_element_input_spisok[1]) + int(list_element_input_spisok[2]) + int(list_element_input_spisok[3])) / 3
        itog_str = str(round(average_ball, 9)) + '\n'
        itog.write(itog_str)
        abiturient_quantity +=1
        subject_one += int(list_element_input_spisok[1])
        subject_two += int(list_element_input_spisok[2])
        subject_three += int(list_element_input_spisok[3])
    average_ball_all_subject = str(round(subject_one / abiturient_quantity, 9)) + ' ' + str(round(subject_two / abiturient_quantity, 9)) + ' ' + str(round(subject_three / abiturient_quantity, 9))
    itog.write(average_ball_all_subject)



