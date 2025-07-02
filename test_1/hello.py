from dop_file import Calculator

if __name__ == '__main__':
    file_name = "/Users/mikearsentev/Docs_on_mac/Проекты/Leet_code/test_1/text_file.txt"
    with open(file_name, "r", encoding="utf-8") as f:
        print("Содержимое файла:")
        for line in f:
            print(line.strip())
    #test = Calculator()
    #print(test.summ(number_1 =int(input("Input number 1: ")),number_2 =int(input("Input number 2: "))))
