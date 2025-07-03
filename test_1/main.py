from dop_file import Calculator
from info import information
import os
if __name__ == '__main__':
    info = information()
    calc = Calculator()
    
    print("""
        1. Math functions,
        2. Create users
        3. Unknown function_1
        4. Unknown function_1  
          """)
    predict = int(input("Input selected point: "))
    if (predict == 1):
        print("""
              We have 4 difirent functions:
              1. +
              2. - 
              3. *
              4. /
              """)
        predict_calc_func = input("Input znak: ")
        if(predict_calc_func =="+"):
            result_func = calc.summ(number_1= int(input("Input number 1: ")),number_2= int(input("Input number 2: ")))
            print(result_func)  
        elif  (predict_calc_func =="-"):    
            result_func = calc.minus(number_1= int(input("Input number 1: ")),number_2= int(input("Input number 2: ")))
            print(result_func)
        elif  (predict_calc_func =="*"):    
            result_func = calc.proizv(number_1= int(input("Input number 1: ")),number_2= int(input("Input number 2: ")))
            print(result_func)
        elif  (predict_calc_func =="/"):    
            result_func = calc.delenie(number_1= int(input("Input number 1: ")),number_2= int(input("Input number 2: ")))
            print(result_func)
    elif (predict == 2):
        result = info.profile_creator(first_name=input("Input name: "), last_name=input("Input last name: "))
    elif (predict == 3):
        result = info.profile_creator(first_name=input("Input name: "), last_name=input("Input last name: "))
    elif (predict == 4): 
        result = info.profile_creator(first_name=input("Input name: "), last_name=input("Input last name: ")) 