def marina_dvigaet_mebel(is_petya_free, is_vasya_free):
    return is_petya_free or is_vasya_free


petya = False
vasya = False

marina_dvigaet_mebel(petya, vasya)

result = marina_dvigaet_mebel(petya, vasya)


print(f"Получится ли перетащить мебель?, {result}")
