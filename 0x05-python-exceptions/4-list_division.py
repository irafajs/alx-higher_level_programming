def list_division(my_list_1, my_list_2, list_length):
    result = []
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
    for i in range(list_length):
        try:
            elem1 = my_list_1[i] if i < len(my_list_1) else 0
            elem2 = my_list_2[i] if i < len(my_list_2) else 0
            c_i_elem1 = isinstance(elem1, (int, float))
            c_i_elem2 = isinstance(elem2, (int, float))
            if not c_i_elem1 or not c_i_elem2:
                raise TypeError("wrong type")
            if elem2 == 0:
                raise ZeroDivisionError("division by 0")
            result.append((elem1 / elem2))
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
