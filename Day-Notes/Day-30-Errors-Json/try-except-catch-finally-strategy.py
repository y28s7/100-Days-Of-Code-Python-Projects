# FileNotFound Error

# try:
#     file = open("a_file.txt")
#
#     dict = {1:2}
#     print(dict[1])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # Raise errors
#     raise KeyError("haha")


# Situation where you would purposefully raise an error
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)

