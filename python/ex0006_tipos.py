# Aula 6 – Tipos Primitivos e Saída de Dados
""" Built-in Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
Getting the Data Type
You can get the data type of any object by using the type() function:
"""
value = 'Sidney'
print(type(value))  # str "string"

num1 = 9
num2 = 8
print(type(num1))
print(type(num2))
mult = num1 * num2


print('A multiplicação de: {} X {} = {}'.format(num1, num2, mult))
print('A multiplicação de: {0} X {1} = {2}'.format(num1, num2, mult))

valuePi = 3.14
print(type(valuePi))  # float

isNum = False
