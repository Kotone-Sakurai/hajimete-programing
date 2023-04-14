dog_name = input("Cloud you tell me your dog's name, please? ")
dog_age = input("and also the age of dog, please? ")

print("ok, your dog '" + dog_name + "' is " + dog_age + " years old.")

#human_age = dog_age*7
human_age = int(dog_age) *7
print(human_age)

print("so your dog '" + dog_name + "' is " + str(human_age) + " years old in human age.")
