is_petya_free = True
is_vasya_free = False


def can_move_furniture(is_petya_free, is_vasya_free):
    return is_petya_free or is_vasya_free


result = can_move_furniture(is_petya_free, is_vasya_free)
print(f"Получится ли перетащить мебель? – {result}")
