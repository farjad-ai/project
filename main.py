import re
from datetime import datetime

def validate_name(name):
    return re.match(r"^[A-Za-z]{3,30}$", name)
print(validate_name("bmw"))
print(validate_name("123"))
print(validate_name("o"))
print(validate_name("be2"))

def validate_model(model):
    return re.match(r"^[A-Za-z]{3,30}$",model)
print(validate_model("mvm"))
print(validate_model("b"))

def validate_color(color):
    return color in ["black","white","red"]
print(validate_color("black"))
print(validate_color("white"))
print(validate_model("red"))
print(validate_color("pink"))

def validate_plate(plate):
    return re.match(r"^[0,9]{2}\s}[آ-ی]\s[0,9]{3}\sایران\s[0,9]{2}$",plate)
print(validate_plate("tyuiol77"))

def validate_datetime_now(now):
    now=datetime.now(now)
print("datetime.now")
if datetime.now:
    print("the time is valid")
else:
    print("the time is invalid")


