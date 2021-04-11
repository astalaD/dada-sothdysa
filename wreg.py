import math
z = input("я умею додавать(+) отнимать(-) множыть(*) делить(/) вознесение до степени(^) корень(|) квадратных уравнений(D) что из етого?")
        
if z == "+":
    x = int(input("перваэ число"))
    y = int(input("второе число"))
    r = (x+y)
if z == "/":
    x = int(input("перваэ число"))
    y = int(input("второе число"))
    if y == (0):
        print("чот нето братончик")
        r = (0)
    else:
        r = (x/y)
if z == "*":
    x = int(input("перваэ число"))
    y = int(input("второе число"))
    r = (x*y)
if z == "-":
    x = int(input("перваэ число"))
    y = int(input("второе число"))
    r = (x-y)
if z== "^":
    x = int(input("число"))
    y = int(input("В какую степень"))
    r = (x ** y)
if z== "|":
    x = int(input("число"))
    r = (math.sqrt(x))
if z == "D":
    a = int(input("в ведите a"))
    b = int(input("в ведите b"))
    c = int(input("в ведите c"))
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"x1={x1} \n x2={x2}")
    if D == 0:
        x = (-b / (2 * a))
        print(f"x = {x} ")
    else:
        print("Корней нет")
    r = (0)
else:
    print("чот нето братончик")
    r = (0)
print(f"результат:{+ r}")
