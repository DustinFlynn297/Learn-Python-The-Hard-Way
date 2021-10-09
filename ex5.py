name = 'Zed A. Shaw'
age = 35 #years
height = 74.00 #inches
weight = 180.00 #pounds
height_in_centimeters = height * 2.54
weight_in_kilos = weight * .453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall and {height_in_centimeters} centimeters tall.")
print(f"He's {weight} pounds heavy in pounds and {weight_in_kilos} in kilograms.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f'If I add {age}, {height}, and {weight} I get {total}.')