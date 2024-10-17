# Stings are immutable (does not change)
a = "Dilesh"
print("Length    :", len(a))
print("Uppercase :", a.upper())
print("Lowercase :", a.lower())
print("\n")


b = "hello !!!!!"
print(b.rstrip("!"))
b = "!!! hello"
print(b.rstrip("!"))
print("\n")


c = "English"
d = "English is a good language. English is communicable."
print(c.replace("English", "Hindi"))
print(d.replace("English", "Hindi"))
print("\n")


e = "I am a good boy"
print(e.split())
print("\n")


f = "i am happy"
g = "this One is Best"
print(f.capitalize())
print(g.capitalize())
print("\n")


h = "* Welcome to our new Channnel *"
print("Length(before) : ", len(h))
print(h.center(40))
print("Length(after)  : ", len(h.center(40)))
print("\n")


i = "He is a good boy. He cooks very well. He dances too"
print(i.count("he"))
print(i.count("He"))
print("\n")


j1 = "This is a pretty code !"
print(j1.endswith("!"))
print(j1.endswith("#"))
j2 = "This is a pretty code !"
print(j2.startswith("This"))
print(j2.startswith("is"))
k = "This is a pretty code !"
print(k.endswith("is", 1, 7))
print("\n")


l = "Don is don"
print(l.find("is"))
print(l.find("h"))    # --> -1
print(l.index("is"))
# print(l.index("h")) # --> error
print("\n")


m1 = "ThisisDilesh2003"
m2 = "This is Dilesh"
m3 = "ThisisDilesh"
m4 = "This is Dilesh 455"
m5 = "ThisisDilesh***"
print(m1.isalnum())
print(m2.isalnum())
print(m3.isalnum())
print(m4.isalnum())
print(m5.isalnum())
print("\n")


n1 = "ThisisDilesh"
n2 = "This is Dilesh"
n3 = "ThisisDilesh2003"
print(n1.isalpha())
print(n2.isalpha())
print(n3.isalpha())
print("\n")


o1 = "This is Dilesh"
o2 = "THIS IS DILESH"
print(o1.isupper())
print(o2.isupper())
print("\n")


o1 = "This is Dilesh"
o2 = "this is dilesh"
print(o1.islower())
print(o2.islower())
print("\n")


p1 = "This is Dilesh"
p2 = "This is Dilesh\n"
print(p1.isprintable())
print(p2.isprintable())
print("\n")


q1 = "  "
q2 = ""
q3 = "This is Dilesh"
print(q1.isspace())
print(q2.isspace())
print(q3.isspace())
print("\n")


r1 = "This is a Dilesh"
print(r1.title())

r2 = "This is a Dilesh"
r3 = "This Is A Dilesh"
print(r2.istitle())
print(r3.istitle())
print("\n")


t = "This is a Dilesh"
print(t.swapcase())
print("\n")


j = "This is a Dilesh"
print(j.replace('i', '*'))
print("\n")
k = "This is a good boy"
print(k.replace('i', '*', 1))
print("\n")
