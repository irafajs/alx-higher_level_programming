def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        if len(my_list_1) > len(my_list_2):
            list_length = len(my_list_1)
        else:
            list_length = len(my_list_2)
        for item in range(list_length):
            s_item1 = my_list_1[item] if item < len(my_list_1) else 0
            s_item2 = my_list_2[item] if item < len(my_list_2) else 1
            s_item1_isint = isinstance(s_item1, (int, float))
            s_item2_isint = isinstance(s_item2, (int, float))
            if not (s_item1_isint and s_item2_isint):
                print("wrong type")
                result.append(0)
            else:
                try:
                    division_result = s_item1 / s_item2
                    result.append(division_result)
                except ZeroDivisionError:
                    print("division by 0")
                    result.append(0)
    except IndexError:
        pass
    finally:
        if len(result) > len(my_list_1) or len(result) > len(my_list_2):
            print("out of range")
        return result
