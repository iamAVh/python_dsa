def is_leap(year):
    if year % 400 ==0:
        return True
    elif year % 100 ==0:
        return False
    elif year % 4 ==0 :
        return True
    else:
        return False

year = int(input("ENter year "))
print(is_leap(year))


# def is_leap(year):
#     return year % 400 ==0 or (year%4==0and year % 100 !=0)

# year = int(input("ENter year "))
# print(is_leap(year))
