import random

ip_22_1 = ['Бобровская Анастасия Дмитриевна',
'Винговатов Александр Олегович',
'Дережинцева Алина Александровна',
'Иохим Рудольф Давыдович',
'Капустин Кирилл Максимович',
'Кожевников Марк Евгеньевич',
'Меркулов Владимир Сергеевич']

ip_22_2 = ['Козмеренко Константин',
'Кондратенко Дмитрий Александрович',
'Морочка Сергей Сергеевич',
'Перетятько Алексей Константинович',
'Поселова Полина Вадимовна',
'Рожков Иван Александрович',
'Рылякова Дарья Максимовна',
'Сагайдак Иван Вячеславович',
'Сапельников Денис Алексеевич',
'Тарасенко Юлия Юрьевна',
'Трубин Данил Владимирович',
'Федулов Дмитрий Игоревич',
'Халоков Богдан Абдуразокович',
'Цапко Глеб Борисович',
'Четверикова Олеся Александровна']

ip_22 = []
ip_22.extend(ip_22_1)
ip_22.extend(ip_22_2)

d = random.choice(ip_22)
print(d)

#test