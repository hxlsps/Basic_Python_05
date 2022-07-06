#Bai 1
first_test_score=float(input('First test score: '))
second_test_score=float(input('Second test score: '))
third_test_score=float(input('Third test score: '))
average_test_score=(first_test_score+second_test_score+third_test_score)/3
print(f'Average Test score is: {average_test_score}')
if average_test_score >=95:
    print('Congratulation')