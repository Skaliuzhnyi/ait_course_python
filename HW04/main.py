is_petya_free = 10
is_vasya_free = False


def can_move_furniture(is_petya_free, is_vasya_free):
    return is_petya_free or is_vasya_free
    # if is_petya_free or is_vasya_free:
    #   return True


result = can_move_furniture(is_petya_free, is_vasya_free)
print(f"Получится ли перетащить мебель? – {result}")
print(result)
print(type(result))
print(is_petya_free)
print(type(is_petya_free))
