from dop_file import Calculator
from info import information
if __name__ == '__main__':
    info = information()
    result = info.profile_creator(first_name=input("Input name: "), last_name=input("Input last name: "))
