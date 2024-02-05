my_img = ('1920', '1080' )

my_another_img = ('1920', '1080', True)
#Example 1
def info(typle):
     return f"{typle[0]}x{typle[1]}" if len(typle) == 2 else "Incorrect image formating."

#print(info(my_another_img))
#Example 2
if len(my_img) == 2:
     print(f"{my_img[0]}x{my_img[0]}")
else:
     print("Incorrect image formating.")

#Example 3
my_str = "Short string"

print(my_str) if len(my_str) < 79 else print("Strig is long")

#info = f"{my_another_img[0]}x{my_another_img[1]}" if len(my_another_img) == 2 else print("Incorrect image formating.")

#print(f"{my_another_img[0]}x{my_another_img[1]}") if len(my_another_img) == 2 else print("Incorrect image formating.")

#print(f"{my_img[0]}x{my_img[1]}") if len(my_img) == 2 else print("Incorrect image formating.")
