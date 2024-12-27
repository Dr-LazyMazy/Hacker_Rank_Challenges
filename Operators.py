def solve(meal_cost, tip_percent, tax_percent):
    #calculate the "tip, tax, and total_cost" from the given equations in the question
    tip = (tip_percent / 100) * meal_cost

    tax = (tax_percent / 100) * meal_cost

    total_cost = meal_cost + tip + tax

    #round the total cost to the nearest int
    rounded_total_cost = round(total_cost)


    print(rounded_total_cost)