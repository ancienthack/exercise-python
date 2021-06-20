def convert(number):
    return ''.join(drop for divisor, drop in
                   {3: "Pling", 5: "Plang", 7: "Plong"}.items()
                   if number % divisor == 0) or str(number)

# using list of tuples for pre-3.7
# def convert(number):
#     return ''.join(drop for divisor, drop in
#                    [(3, "Pling"), (5, "Plang"), (7, "Plong")]
#                    if number % divisor == 0) or str(number)

# the above use or on the falsiness of an empty string
# the below use a ternary expression

# def convert(number):
#     msg = ''.join(drop for divisor, drop in {3: "Pling", 5: "Plang", 7: "Plong"}.items() if number % divisor == 0)
#     return msg if msg != '' else str(number)

# using list of tuples for pre-3.7
# def convert(number):
#     msg = ''.join(drop for divisor, drop in [(3, "Pling"), (5, "Plang"), (7, "Plong")] if number % divisor == 0)
#     return msg if msg != '' else str(number)