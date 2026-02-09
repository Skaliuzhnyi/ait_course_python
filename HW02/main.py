eur_to_usd = 1.09
cookies_price = 3.25
waffles_price = 4.40
cookies_kg = 0.5
waffles_kg = 1.5
money_eur = 10
total_usd = cookies_kg * cookies_price + waffles_kg * waffles_price
total_eur = total_usd / eur_to_usd
result_eur = money_eur - total_eur
print(round(result_eur, 2))
