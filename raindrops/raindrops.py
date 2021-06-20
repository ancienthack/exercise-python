# my solution
def convert(number):
    n = number
    # if n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    #     return str(n)
    if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
        return 'PlingPlangPlong'
    if n % 3 == 0 and n % 5 == 0 and n % 7 != 0:
        return 'PlingPlang'
    if n % 3 == 0 and n % 5 != 0 and n % 7 == 0:
        return 'PlingPlong'
    if n % 3 != 0 and n % 5 == 0 and n % 7 == 0:
        return 'PlangPlong'
    if n % 3 == 0 and n % 5 != 0 and n % 7 != 0:
        return 'Pling'
    if n % 3 != 0 and n % 5 == 0 and n % 7 != 0:
        return 'Plang'
    if n % 3 != 0 and n % 5 != 0 and n % 7 == 0:
        return 'Plong'
    else:
        return str(n)

# mentor solution
def convert(number):
    return ''.join(drop for divisor, drop in
                   {3: "Pling", 5: "Plang", 7: "Plong"}.items()
                   if number % divisor == 0) or str(number)