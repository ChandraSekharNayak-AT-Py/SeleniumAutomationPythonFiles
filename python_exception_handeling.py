# a = int(input('Enter your number:-'))
# b = int(input('Enter your number:-'))
# c = 1
# try:
#     print(a/b)
# except TypeError:
#     print(a/c)
# except NameError:
#     print(a/c)
# except Exception:
#     print(a/c)


# How to print exception information

# a = int(input('Enter your number:-'))
# b = int(input('Enter your number:-'))
# c = 1
# try:
#     print(a/b)
# except Exception as msg:
#     print(a/c,msg)

# print(10/0)


#Single Except Block can handel multiple except block

a = eval(input('Enter your number:-'))
b = eval(input('Enter your number:-'))
c = 1

try:
    print(a/b)
except (ZeroDivisionError,TypeError) as msg:
    print(msg)

finally:
    #cleanup code or excute code
    print(a**b)
