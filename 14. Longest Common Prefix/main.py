def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Берём первую строку как базу для сравнения
    prefix = strs[0]

    # Сравниваем с каждой следующей строкой
    for s in strs[1:]:
        # Урезаем префикс, пока он не совпадёт с началом строки s
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # отрезаем последний символ
            if not prefix:
                return ""  # если префикс стал пустым — общего нет
    
    return prefix

strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))