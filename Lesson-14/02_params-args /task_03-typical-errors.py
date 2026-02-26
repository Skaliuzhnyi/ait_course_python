def area(w, h):
  return w * h
    
print(area(10, 20))

# !! TypeError: area() missing 1 required positional argument: 'h'
# print(area(10))  

# !! TypeError: area() takes 2 positional arguments but 3 were given
# print(area(10, 20, 30))

# !! TypeError: area() got multiple values for argument 'w'
# print(area(10, w=20))