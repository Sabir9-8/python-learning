#A soft keyword only acts as a keyword if the parser determines the context requires it. Everywhere else, it acts as a normal variable. e.g(match, case)

# 'match' is used as a standard variable identifier (Perfectly legal!)
match = "pattern found"

status_code = int(input("Enter the code: "))
# 'match' is used as a keyword here because of the structural context
match status_code:
    case 200:
        print("Success")
    case _:
        print("Unknown")
