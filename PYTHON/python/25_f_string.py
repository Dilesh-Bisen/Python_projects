# String formatting in python : String formatting can be done in python using the format method.

# f-strings in python : It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings(f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier. When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

print("\nString Formating : ")
str = "hey my name is {} and I am a {} boy"
str1 = "Dilesh"
str2 = "good"
print(str.format(str1, str2))
# or 
# str = "hey my name is {1} and I am a {0} boy"
# str1 = "Dilesh"
# str2 = "good"
# print(str.format(str2, str1))

txt = "For only {price:.2f} dollars!"
print(txt.format(price=49.059876))

print("\nF-String : ")
str = "hey my name is {} and I am a {} boy"
str1 = "Dilesh"
str2 = "good"
print(f"hey my name is {str1} and I am a {str2} boy")

price=49.059876
print(f"For only {price:.4f} dollars!")

print(f"{60*2}")
print(type(f"{60*2}"))

print("My {name} is {Dilesh}")
print(f"My {{name}} is {{Dilesh}}")