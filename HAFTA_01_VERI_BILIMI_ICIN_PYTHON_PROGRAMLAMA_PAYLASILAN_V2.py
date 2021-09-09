###############################################
# ÇALIŞMA ORTAMI AYARLARI (SETTING UP WORKING ENVIRONMENT)
###############################################
# - Python'a Giriş ve PyCharm
# - Virtual Environments (conda)
# - Dependency Management (conda, pip) (Buraya kadar 1 saat)
# - Python İlk Adımlar


###############################################
# PYTHON'A GİRİŞ ve PyCharm
###############################################

###############################################
# VIRTUAL ENVIRONMENTS (CONDA)
###############################################

###############################################
# DEPENDENCY MANAGEMENT (CONDA, PIP)
###############################################

###############################################
# PYTHON İLK ADIMLAR
###############################################

# - Sayılar (Numbers) ve Karakter Dizileri (Strings)
# - Atamalar ve Değişkenler (Assignments & Variables)
# - Yazdırma Türleri (Print Types)
# - Kullanıcıdan Bilgi Almak: Input

###############################################
# Sayılar (Numbers) ve Karakter Dizileri (Strings)
###############################################

# string
# print("Hello AI Era")

# integer
9

# float
9.2

# types
type(9)
type(9.2)
type("123")

###############################################
# Atamalar ve Değişkenler (Assignments & Variables)
###############################################

a = 9
b = 10

a * b
a - b

hi = "Hello AI Era"

# del hi

###############################################
# Yazdırma Türleri (Print Types)
###############################################

# print
print("hello ai era")
name = "Rode"
age = 35
print(name, age)

# %
"Name: %s" % name
"Name: %s Age: %s" % (name, age)

# str.format()
"Name: {} Age: {}".format(name, age)

person = {"name": "Rode", "age": 35}
"Name:{} Age: {}".format(person["name"], person["age"])

# fstring
F"Name: {name} Age: {age}"

###############################################
# Kullanıcıdan Bilgi Almak: Input
###############################################

number = input()
type(number)

number * 3
# number / 3

int(number) / 3

num1 = int(input())
num2 = int(input())

num1 * num2

###############################################
# VERİ YAPILARI (DATA STRUCTURES)
###############################################
# - Veri Yapılarına Giriş ve Hızlı Özet
# - Sayılar (Numbers): int, float, complex
# - Karakter Dizileri (Strings): str
# - Boolean (TRUE-FALSE): bool
# - Liste (List)
# - Sözlük (Dictionary)
# - Demet (Tuple)
# - Set


###############################################
# Veri Yapılarına Giriş ve Hızlı Özet
###############################################

# Sayılar: integer
x = 46
type(x)

# Sayılar: float
x = 10.3
type(x)

# Sayılar: complex
x = 2j + 1
type(x)

# String
x = "Hello ai era"
type(x)

# Boolean
True
False
type(True)
5 == 4
3 == 2
1 == 1
type(3 == 2)

# Liste
x = ["btc", "eth", "xrp"]
type(x)

# Sözlük (dictionary)
x = {"name": "Peter",
     "Age": 36}

type(x)

# Tuple
x = ("python", "ml", "ds")
type(x)

# Set
x = {"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, set ve dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.

###############################################
# Sayılar (Numbers): int, float, complex
###############################################

a = 5
b = 10.3
a * 3
a / 6
a * b / 10
a ** 2

#######################
# Tipleri değiştirmek
#######################

int(b)
float(a)
int(a * b / 10)

###############################################
# Karakter Dizileri (Strings)
###############################################

print("John")
print('John')

name = "John"
name = 'John'

#######################
# Çok Satırlı Karakter Dizileri
#######################

"""Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizileri (Strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

long_str = """Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizileri (Strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

name = "John"
name[0]
name[3]
name[4]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

name[0:2]

#######################
# String İçerisinde Karakter Sorgulamak
#######################

long_str = """Veri Yapıları: Hızlı Özet,
Sayılar (Numbers): int, float, complex,
Karakter Dizileri (Strings): str,
List, Dictionary, Tuple, Set,
Boolean (TRUE-FALSE): bool"""

"bool" in long_str

"boolu" in long_str

###############################################
# String Metodları
###############################################

dir(str)
dir("mvk")

#######################
# len
#######################

# len()
type(len)

name = "john"
len(name)
len("MVK")
len("1")

#######################
# upper() & lower(): küçük-büyük dönüşümleri
#######################

"mvk".upper()
"JOHN".lower()

# type(upper())

#######################
# replace: karakter değiştirir
#######################

hi = "Hello AI Era"
hi.replace("l", "p")
hi = hi.replace("l", "p")

#######################
# split: böler
#######################

"Hello AI Era".split()

#######################
# strip: kırpar
#######################

" ofofo ".strip()
"ofofo".strip("o")

#######################
# capitalize: ilk harfi büyütür
#######################

"foo".capitalize()

#######################
# isalnum: alfabetik mi ya da nümerik mi kontrolü
#######################

"foo".isalnum()

#######################
# isnumeric: nümerik mi kontrolü yapar
#######################

"foo".isnumeric()
"99".isnumeric()

# Buraya kadar 1 saat.

###############################################
# Liste (List)
###############################################

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v"]

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
notes[0]
notes[0:4]

notes[0] = 99

not_nam[6][1]

###############################################
# Liste Metodları (List Methods)
###############################################

dir(notes)

#######################
# len: builtin python fonksiyonu, boyut bilgisi.
#######################

len(notes)

#######################
# append: eleman ekler
#######################

notes.append(90)

#######################
# pop: indexe göre siler
#######################

notes.pop(0)

#######################
# insert: indexe ekler
#######################

notes.insert(2, 99)

###############################################
# Sözlük (Dictonary)
###############################################

# - Değiştirilebilir.
# - Sırasız. (3.7 sonra sıralı.)
# - Kapsayıcı.

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

#######################
# Key Sorgulama
#######################

"REG" in dictionary

#######################
# Key'e Göre Value'ya Erişmek
#######################

dictionary["REG"]
dictionary.get("REG")

#######################
# Value Değiştirmek
#######################

dictionary["REG"] = 11

#######################
# Tüm Key'lere Erişmek
#######################

dictionary.keys()

#######################
# Tüm Value'lara Erişmek
#######################

dictionary.values()

#######################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
#######################

dictionary.items()

#######################
# Key-Value Değerini Güncellemek
#######################

dictionary.update({"REG": 112})

#######################
# Yeni Key-Value Eklemek
#######################

dictionary.update({"RF": 10})

#######################
# Key ile Bir Item'ın Silinmesi
#######################

dictionary.pop("RF")

###############################################
# Demet (Tuple)
###############################################

# Listelerin değişime kapalı kardeşidir.

# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("john", "mark", 1, 2)
t[0:3]

names[0] = "999"
t[0] = "999"

t = list(t)
t[0] = "999"
t = tuple(t)

###############################################
# Set
###############################################

# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

###############################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
###############################################
# - Fonksiyonlar (Functions)
# - Koşullar (Conditions)
# - Döngüler (Loops)
# - Comprehesions
# - Lambda, Map, Reduce, Filter

###############################################
# FONKSİYONLAR (FUNCTIONS)
###############################################

#######################
# Fonksiyon nedir?
#######################

#######################
# Fonksiyon Okuryazarlığı
#######################

print("a")

# ?print
help(print)

print("a", "b")

print("a", "b", sep="_")


#######################
# Fonksiyon Tanımlama
#######################

def calculate(x):
    print(x * 2)


calculate(5)


# İki argümanlı/parametreli bir fonksiyon tanımlayalım.

def summer(arg1, arg2):
    print(arg1 + arg2)
    print(arg1 - arg2)
    print(arg1 * arg2)


summer(7, 8)


#######################
# Docstring
#######################

def summer(arg1, arg2):
    """
    Sum of two numbers

    args:
    -----
          arg1: int, float
          arg2: int, float

    """
    print(arg1 + arg2)


help(summer)

summer(7, 8)
summer(77, 88)


#######################
# Fonksiyonların Statement/Body Bölümü
#######################

# def function_name(parameters/arguments):
#     statements (function body)

def multiplication(a, b):
    c = a * b
    print(c)


multiplication(8, 9)


def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")


say_hi()

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(10, 9)

add_element(18, 1)

add_element(a=180, b=1)


#######################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#######################
def divide(a, b=1):
    print(a / b)

divide(1)


#######################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
#######################

# varm, moisture, charge

(56 + 15) / 80
(17 + 45) / 70
(17 + 45) / 70

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(90, 12, 12)
calculate(17, 45, 70)

#######################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
#######################

calculate(17, 45, 70) * 10

type(calculate(17, 45, 70))
type(10)

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

calculate(90, 12, 12) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p

standardization(10, 9)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)

all_calculation(10, 90, 87, 10)

#######################
# Lokal & Global Değişkenler (Local & Global Variables)
#######################

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)

add_element(10, 8)


#######################
# Doğru Fonksiyon Yazımı
#######################

# PEP8
# DRY (dont repeat yourself)
# DoT (Do one Thing)
# Modularity

# Buraya kadar 1 saat.

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

###############################################
# KOŞULLAR (CONDITIONS)
###############################################

#######################
# if
#######################

1 == 1
1 == 2

if 1 == 1:
    print("something")

number = 12

if number == 10:
    print("Koşul sağlanmaktadır")


def number_check(number):
    if number == 10:
        print("Koşul sağlanmaktadır")

number_check(90)


#######################
# else
#######################

def number_check(number):
    if number == 10:
        print("equal to 10")
    else:
        print("not equal to 10")

number_check(9)

#######################
# elif
#######################

def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number_check(9)
number_check(11)
number_check(10)


###############################################
# DÖNGÜLER (LOOPS)
###############################################

students = ["John", "Mark", "Venessa", "Mariam"]

students[0]
students[1]
students[2]
students[3]

type(students[0])
students[0].upper()
students[1].upper()
students[2].upper()

for student in students:
    print(student)

for student in students:
    print(student.upper())

for student in students:
    print(student + "_")

for student in students:
    print(F"Old Name: {student}, New Name: {student.upper()}")

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)


1000 * 20 / 100 + 1000
2000 * 20 / 100 + 2000
3000 * 20 / 100 + 3000

def new_salary(x):
    return int(x * 20 / 100 + x)

new_salary(1000)

def new_salary(salary, rate=20):
    return int(salary * rate / 100 + salary)

new_salary(10000, 50)

for salary in salaries:
    print(new_salary(salary, 40))


def raise_up(x):
    print(int(x * 10 / 100 + x))

raise_up(1000)

def raise_down(x):
    print(int(x * 20 / 100 + x))

raise_down(1000)

for salary in salaries:
    if salary >= 3000:
        raise_up(salary)
    else:
        raise_down(salary)


def new_salary(salary, rate=20):
    print(int(salary * rate / 100 + salary))
    # return int(salary * rate / 100 + salary)

for salary in salaries:
    if salary >= 3000:
        new_salary(salary, rate=10)
    else:
        new_salary(salary, rate=20)


#######################
# Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string'i değiştirmek istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"
#         Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN


for i in range(len("vahit")):
    print(i)


def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()

    print(new_string)

alternating("vahit")

alternating("duygularla yatırım yapılmaz")

alternating("algoritmik trading 101 derki duygu varsa para yok karşim")

alternating("hi my name is john and i am learning python")

#######################
# break & continue & while
#######################

# break: bir koşul sağlandığında durmak için kullanılır.
salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        print("break point")
        break
    print(salary)

# continue: bir koşul yakalandığında iterasyondaki nesne atlanır.

for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# "dığı sürece" şunu yap.
number = 1
while number < 9:
    print(number)
    number += 1

# buraya kadar 45 dk.







#######################
# Enumerate: Otomatik Counter/Indexer ile for loop
#######################

# Problem: Listedeki öğrencileri index numaralarına göre iki gruba bölmek
students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

#######################
# Mülakat Sorusu
#######################

# divide_students işlemini 2 grubu tek bir listede return edecek bir fonksiyonla yapınız.
students = ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)

    return groups

divide_students(students)

#######################
# Enumerate'i Belirli Bir Index ile Kullanmak
#######################

for index, student in enumerate(students, 1):
    print(index, student)

def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students, 1):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)

    return groups

divide_students(students)



#######################
# Mülakat Sorusu
#######################

# Alternating string with enumerate
def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")


#######################
# Zip
#######################

students = ["John", "Mark", "Venessa", "Mariam"]
departments = ["mathematics", "statistics", "physics", "astronomy"]
ages = [23, 30, 26, 22]

print(list(zip(students, departments, ages)))

###############################################
# lambda, map, filter, reduce
###############################################

def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b

new_sum(7, 8) * 9

# MAP
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2, salaries))

list(map(lambda x: x.upper(), "john"))

# # FILTER
# # 6%2 == 0
# list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list(filter(lambda x: x % 2 == 0, list_store))
#
# # REDUCE
# from functools import reduce
# list_store = [1, 2, 3, 4]
# reduce(lambda a, b: a + b, list_store)


# buraya kadar 20 dk.




###############################################
# COMPREHENSIONS
###############################################

#######################
# List Comprehension
#######################

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))


null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))


[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary > 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

# çirkin
students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

#######################
# Dictionary Comprehension
#######################

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dictionary["a"]
dictionary["b"]

dictionary.keys()
dictionary.values()
dictionary.items()


for value in dictionary.values():
    print(value*5)

# value'lara işlem yapmak
{k: v*5 for (k, v) in dictionary.items()}

# key'lere işlem yapmak
{k.upper(): v*5 for (k, v) in dictionary.items()}


#######################
# Döngü kullanarak sözlüğe eleman eklemek
#######################

#######################
# Mülakat Sorusu
#######################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.

numbers = range(10)

for i in numbers:
    print(i)

new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}

#######################
# List & Dict Comprehension Uygulamalar
#######################

#######################
# Amaç: Bir Veri Setindeki Değişken İsimlerini Değiştirmek
#######################


# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

#######################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
#######################


# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']


df.columns

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]


#######################
# Categorical Değişkenlerin Başına CAT yazmak.
#######################


# before:
# ['total',
# 'speeding',
# 'alcohol',
# 'not_distracted',
# 'no_previous',
# 'ins_premium',
# 'ins_losses',
# 'abbrev']

# after:
# ['TOTAL',
#  'SPEEDING',
#  'ALCOHOL',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM',
#  'INS_LOSSES',
#  'CAT_ABBREV']

df = sns.load_dataset("car_crashes")

[col for col in df.columns if df[col].dtype == "O"]

["CAT_" + col.upper() if df[col].dtype == "O" else col.upper() for col in df.columns]


#######################
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
#######################


# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

num_cols = [col for col in df.columns if df[col].dtype != "O"]

soz = {}

agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

{col: ["mean", "min", "max", "sum"] for col in num_cols}

# uygulama

new_dict = {col: agg_list for col in num_cols}
df.groupby("abbrev").agg(new_dict)

# uygulama 2

df = sns.load_dataset("tips")
df.head()
num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

new_dict = {col: agg_list for col in num_cols}

df.groupby("time").agg(new_dict)

#######################
# Amaç: Value bölümündeki listenin her bir elemanını dinamik olarak biçimlendirmek
#######################

#######################
# Mülakat Sorusu
#######################


# before:
# {'total': ['mean', 'min', 'max', 'sum'],
#  'speeding': ['mean', 'min', 'max', 'sum'],
#  'alcohol': ['mean', 'min', 'max', 'sum']}

# after:
# {'total': ['total_mean', 'total_min', 'total_max', 'total_var'],
#  'speeding': ['speeding_mean', 'speeding_min', 'speeding_max', 'speeding_var'],
#  'alcohol': ['alcohol_mean', 'alcohol_min', 'alcohol_max', 'alcohol_var']

df = sns.load_dataset("car_crashes")
num_cols = [col for col in df.columns if df[col].dtype != "O"]
agg_list = ["mean", "min", "max", "sum"]


{col: [str(col) + "_" + c for c in agg_list] for col in num_cols}



###############################################
# AMAC: Bir listenin ilk elemanını key diğer elemanların tamamını da value olarak atamak
###############################################

#######################
# Mülakat Sorusu
#######################

# before
#    total  speeding  alcohol  not_distracted  no_previous
# 0   18.8     7.332    5.640          18.048       15.040
# 1   18.1     7.421    4.525          16.290       17.014
# 2   18.6     6.510    5.208          15.624       17.856
# 3   22.4     4.032    5.824          21.056       21.280
# 4   12.0     4.200    3.360          10.920       10.680


# after:
# {18.8: [7, 5, 18, 15],
#  18.1: [7, 4, 16, 17],
#  18.6: [6, 5, 15, 17],
#  22.4: [4, 5, 21, 21],
#  12.0: [4, 3, 10, 10]}


df = sns.load_dataset("car_crashes")
num_cols = [col for col in df.columns if df[col].dtype in [int, float]]

df[num_cols].head()

{row[0]: [int(s) for s in row[1:]] for row in df[num_cols].values}



df.head()

# buraya kadar 1 saat



# BAKILMASINA GEREK YOKTUR. NOT OLARAK BIRAKTIM.

###############################################
# DECORATOR: decorators wrap a function, modifying its behavior.
###############################################

# Functions as arguments
def say_hi(name):
    return f"Hello {name}!"

say_hi("John")

def talk(func):
    return func("John")

talk(say_hi)

def say_hey(name):
    return f"Hey hey {name}!"

talk(say_hey)




# Inner Functions: define functions inside other functions
def meeting():
    print("Hi guys! I am the host")

    def hi_from_john():
        print("Hello!")

    def hi_from_erik():
        print("Hey hey!")

    hi_from_john()
    hi_from_erik()


meeting()

# Peki hi_from_john fonksiyonuna erişmeye çalışalım:
# hi_from_john()

# Neden çünkü meeting'in içerisinde.

# Returning Functions From Functions
def meeting():
    print("Hi guys! I am the host")

    def hi_from_john():
        print("Hello!")

    def hi_from_erik():
        print("Hey hey!")

    hi_from_john()
    hi_from_erik()

    return hi_from_john, hi_from_erik


hi_from_john, hi_from_erik = meeting()

hi_from_john()
hi_from_erik()


# Basic Decorator Template
# decorators wrap a function, modifying its behavior.
def my_decorator(func):
    def wrapper():
        print("Do something before the function call.")
        func()
        print("Do something after the function call.")
    return wrapper

def say_hi():
    print("Hello!")

say_hi = my_decorator(say_hi)
say_hi()

# Other usage
@my_decorator
def say_hi():
    print("Hello!")

say_hi()

# fonksiyonun ismi nedir?
say_hi
say_hi.__name__

# naming for actual function
import functools
def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Do something before the function call.")
        func()
        print("Do something after the function call.")
    return wrapper

@my_decorator
def say_hi():
    print("Hello!")

say_hi()
say_hi.__name__


# Decorating Functions With Arguments
@my_decorator
def say_hi(name):
    print("Hello!", name)


say_hi("MVK")


# fonksiyona arguman olarak verdik ama bir arguman vereceğimizi decorator fonksiyona söylemedik.
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Do something before the function call.")
        func(*args, **kwargs)
        print("Do something after the function call.")
    return wrapper

@my_decorator
def say_hi(name):
    print("Hello!", name)


say_hi("MVK")

# Final decorator template:
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Do something before the function call.")
        func(*args, **kwargs)
        print("Do something after the function call.")
    return wrapper



# PARTY BOY DECORATOR
def party_boy(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Welcome our home!")
        func(*args, **kwargs)
        print("Bye bye!")
    return wrapper

# şimdi party boy ile decorate edilmiş bir organizasyon yapalım.
@party_boy
def do_party():
    print("Eat, meet, play")

do_party()

# başka parti düzenlemek isteyen birisi var. partisini decorate ettirmek istiyor.
@party_boy
def do_corona_party():
    print("Do someting silly")

do_corona_party()

# REAL WORLD EXAMPLE: TIMING FUNCTION

import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def sum_of_even_numbers(numbers):
    even_sum = 0
    for number in range(numbers):
        if number % 2 == 0:
            even_sum += number
    return even_sum


sum_of_even_numbers(10)
sum_of_even_numbers(100*100)
sum_of_even_numbers(100*10000)


###############################################
# ÖDEV 1: Komut satırından Python kodu çalıştırma.
###############################################

# Yazacak olduğunuz "py" uzantılı bir python dosyasını komut satırından çalıştırmanız beklenmektedir.
# Örneğin hi.py isimli bir dosyanız olsun ve içinde print("isim soy isim") kodu olsun.
# Bilgisayarınızın konsolunu açıp konsoldan hi.py dosyasının olduğu dizine gelip buradan "python hi.py" kodunu
# çalıştırdığınızda ekranınızda "isim soy isim" yazmalı.
# Adım adım nasıl yapılacağı anlatılmıştır.

# Adım 1: PyCharm'da "hi.py" isminde python dosyası oluştur.
# Adım 2: Bu dosyanın içirisine şu kodu kendine göre yaz ve kaydet:
# print("Ben Sinan Artun ÖDEV tamam, bu çok kolaymış")
# Adım 3: Şimdi konsoldan "hi.py" dosyasının olduğu dizine (klasöre) gitmen gerekiyor.
# Neyse ki PyCharm ile bu çok kolay. Sol tarafta yer alan menüde hi.py dosyası hangi klasördeyse
# o klasöre sağ tuş ile tıklayıp şu seçimi yap: "open in > terminal".
# PyCharm'ın alt tarafında terminal ekranı açılacak. Şu anda hi.py dosyası ile aynı dizindesin (klasörde).
# Adım 4: Konsolda şu kodu yazmalısın: python hi.py
# Adım 5: Çıktını ekran görüntüsünü alıp grubunda paylaş.





###############################################
# ÖDEV 2: Kendi adınızda bir virtual environment oluşturunuz ve aşağıdakileri yapınız.
###############################################


###############################################
# Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.
###############################################

###############################################
# Görev 2: Oluşturduğunuz environment'ı aktif ediniz.
###############################################

###############################################
# Görev 3: Yüklü paketleri listeleyiniz.
###############################################

###############################################
# Görev 4: Environment içerisine Numpy'ın güncel versiyonunu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
###############################################

###############################################
# Görev 5: İndirilen Numpy'ın versiyonu nedir?
###############################################

###############################################
# Görev 6: Pandas'ı upgrade ediniz. Yeni versiyon nedir?
###############################################

###############################################
# Görev 7: Numpy'ı environment'tan siliniz.
###############################################

###############################################
# Görev 8: Seaborn kütüphanesini ve matplotlib kütüphanesini aynı anda güncel versiyonları ile indiriniz.
###############################################

###############################################
# Görev 9: Virtual environment içindeki kütüphaneleri versiyon bilgisi ile beraber export ediniz ve yaml dosyasını inceleyiniz.
###############################################

###############################################
# Görev 10: Oluşturduğunuz environment'i siliniz.
###############################################

# İpucu: Önce adınız olan env'ı deactivate ediniz.


###############################################
# ÖDEV 3: List Comprehension Applications
###############################################

###############################################
# Görev 1: car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
###############################################

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns



# Veri setini baştan okutarak aşağıdaki çıktıyı elde etmeye çalışınız.

# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

# Notlar:
# Numerik olmayanların da isimleri büyümeli.
# Tek bir list comp yapısı ile yapılmalı.



###############################################
# Görev 1 Çözüm
###############################################


###############################################
# Görev 2: İsminde "no" BARINDIRMAYAN değişkenlerin isimlerininin SONUNA "FLAG" yazınız.
###############################################

# Tüm değişken isimleri büyük olmalı.
# Tek bir list comp ile yapılmalı.



# Beklenen çıktı:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']

###############################################
# Görev 2 Çözüm
###############################################



###############################################
# Görev 3: Aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçerek yeni bir df oluşturunuz.
###############################################

# df.columns
# og_list = ["abbrev", "no_previous"]

# Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.


# Beklenen çıktı:

# new_df.head()
#
#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630

###############################################
# Görev 3 Çözüm
###############################################