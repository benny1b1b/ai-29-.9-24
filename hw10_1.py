# .1 רשימות comprehension

import random

# a. בשורה אחת - צור רשימה של מספרים מ 95-105

#long way
list95_100: list[int] = []
for i in range(95,101):
    list95_100.append(i)
print(list95_100)

list95_100: list[int] = [i for i in range(95,100+1)]
print(list95_100)


# b. בשורה אחת - צור רשימה של מספרים זוגיים מ 10-20
# כלומר: ,10 ,12 ,14 ,16 ,18 20

list10_20_2: list [int] = [i for i in range(10, 20+2, 2)]
print(list10_20_2)


# c. בשורה אחת - צור רשימה של 5 איברים אקראיים של False True

list_rand5_bol: list[bool] = [random.choice([True,False]) for i in range(5)]
print(list_rand5_bol)


# d. בשורה אחת - צור רשימה של 10 מספרים אקראיים בטווח 1-100

list_rand100: list[int] = [random.randint(1,100) for i in range(10)]
print(list_rand100)


# e. בשורה אחת - מהרשימה שיצרת בסעיף הקודם, צור רשימה המכילה רק את המספרים
# הגדולים מ- 50

list_more50: list[int] = [i for i in list_rand100 if i > 50]
print(list_more50)


# f.* בונוס: האם תוכל בשורה אחת לבצע את 2 הסעיפים הקודמים?

list_rand100: list[int] = [random.randint(1,100) for i in range(10) if random.randint(1,100) > 50]
print(list_rand100)


# g.* בונוס: קלוט מחרוזות מהמשתמש. בשורה אחת צור רשימה המכילה את כל האותיות
# שהקליד חוץ מהאות t וg.* בונוס: קלוט מחרוזות מהמשתמש. בשורה אחת צור רשימה המכילה את כל האותיות
# שהקליד חוץ מהאות t וחוץ מ- רווח.
# לדוגמא אם המשתמש הכניס masters python hello
# ]'h', 'e', 'l', 'l', 'o', 'p', 'y', 'h', 'o', 'n', 'm', 'a', 's', 'e', 'r', 's'[ :הרשימה תהיה התשובהחוץ מ- רווח.

sentence: str = input("enter a sentence: ")
list_sentence: list[str] =[letter for letter in sentence if letter not in ["t", " "]]
print(list_sentence)


# h. בשורה אחת - צור רשימה של 10 מספרים אקראיים בטווח 10-99
# הדפס את הרשימה
# כעת בשורה אחת - צור רשימה של 10 מספרים שיכילו רק את ספרת האחדות של
# האיברים מהרשימה הקודמת. לדוגמא:
# אם הרשימה הראשונה היתה – ,44 ,19 ,99 51 ...
# הרשימה השנייה תהיה – ,4 ,9 ,9 1 ....

list10_rand: list[int] = [random.randint(10,90+1) for i in range(10)]
print(list10_rand)

list10_rand_ahadot: list[int] = [i % 10 for i in list10_rand]
print(list10_rand_ahadot)