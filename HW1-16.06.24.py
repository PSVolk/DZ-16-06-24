def merge_lists(list1, list2, list3, list4):

    return list1 + list2 + list3 + list4

def sort_list(merged_list, order):

    if order == "убывание":
        return sorted(merged_list, reverse=True)
    elif order == "возрастание":
        return sorted(merged_list)
    else:
        raise ValueError("Пиши правильно:'убывание' или 'возрастание'.")

def linear_search(lst, target):

    for i, item in enumerate(lst):
        if item == target:
            return i
    return -1

def main():

    list1 = [1, 3, 5, 7, 9]
    list2 = [2, 4, 6, 8, 10]
    list3 = [11, 13, 15, 17, 19]
    list4 = [12, 14, 16, 18, 20]

    merged_list = merge_lists(list1, list2, list3, list4)
    print("Общий список:", merged_list)

    order = input("Выберите порядок сортировки (убывание/возрастание): ")
    sorted_list = sort_list(merged_list, order)
    print(f"Список отсортирован в  порядке {order}:", sorted_list)

    target = int(input("Введите значение для поиска: "))
    index = linear_search(sorted_list, target)
    if index == -1:
        print(f"Значение {target} не найдено в списке.")
    else:
        print(f"Значение {target} найдено в списке по индексу {index}.")

if __name__ == "__main__":
    main()