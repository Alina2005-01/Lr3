# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    list1 = group1.split(separator)
    list2 = group2.split(separator)

    common_participants = set(list1) & set(list2)
    result = sorted(list(common_participants))
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
result_with_pipe = find_common_participants(participants_first_group, participants_second_group, "|")
print(f"Общие участники с разделителем '|': {result_with_pipe}")

test_group1 = "Иванов,Петров,Сидоров"
test_group2 = "Петров,Сидоров,Смирнов"
result_with_comma = find_common_participants(test_group1, test_group2)
print(f"Общие участники с разделителем по умолчанию ',': {result_with_comma}")