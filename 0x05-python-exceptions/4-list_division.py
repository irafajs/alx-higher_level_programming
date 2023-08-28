def list_division(my_list_1, my_list_2, list_length):
    results = []
    error_messages = []
    try:
        for i in range(list_length):
            elem1 = my_list_1[i] if i < len(my_list_1) else 0
            elem2 = my_list_2[i] if i < len(my_list_2) else 1
            c_int_el1 = isinstance(elem1, (int, float))
            c_int_el2 = isinstance(elem2, (int, float))
            if not (c_int_el1 and c_int_el2):
                error_messages.append("wrong type")
                results.append(0)
            else:
                try:
                    division_result = elem1 / elem2
                    if division_result == 0:
                        results.append(0)
                    else:
                        results.append(division_result)
                except ZeroDivisionError:
                    error_messages.append("division by 0")
                    results.append(0)
    except IndexError:
        pass
    finally:
        if len(my_list_1) < list_length or len(my_list_2) < list_length:
            error_messages.append("out of range")
        for error in error_messages:
            print(error)
        return results
