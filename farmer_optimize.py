"""
Write a generic function to compute various scenarios for the following
optimization problem: A farmer owns X acres of land. She profits P1 dollars per
acre of corn and P2 dollars per acre of oats. Her team has Y hours of labor
available. The corn takes H1 hours of labor per acre and oats require H2 hours
of labor per acre. How many acres of each can be planted to maximize profits?

Test the function for the following cases:
a) X = 240, Y = 320, P1 = $40, P2 = $30, H1 = 2, H2 = 1
b) X = 300, Y = 380, P1 = $70, P2 = $45, H1 = 3, H2 = 1
c) X = 180, Y = 420, P1 = $65, P2 = $55, H1 = 3, H2 = 2
"""


def farm_optimize(farm_acres, farm_hours, corn_prof_per_acre,
                  oats_prof_per_acre, corn_hours, oats_hours):

    resolution = 0.01
    split = resolution
    optimized = False
    debug = False

    while optimized is False and split <= 1:

        corn_acres = farm_acres * split
        oats_acres = farm_acres - corn_acres

        corn_labor = corn_hours * corn_acres
        oats_labor = oats_hours * oats_acres
        total_labor = round(corn_labor + oats_labor, 2)

        if total_labor >= farm_hours:
            optimized = True
        elif total_labor < farm_hours:
            corn_profit = corn_prof_per_acre * corn_acres
            oats_profit = oats_prof_per_acre * oats_acres
            total_profit = int(round(corn_profit + oats_profit, 0))

            if debug:
                print(
                    f"Predicted Labor: {total_labor} Hours,"
                    f" Labor Limit:{farm_hours} Hours")
                print(
                    f"Corn Acres: {corn_acres},"
                    f" Oats Acres: {oats_acres}")
                print(f"Predicted Profit: ${total_profit}\n")

            split += resolution
    return total_profit, round(corn_acres, 2), round(oats_acres, 2)


# Tests
X = [240, 300, 180]
Y = [320, 380, 420]
P1 = [40, 70, 65]
P2 = [30, 45, 55]
H1 = [2, 3, 3]
H2 = [1, 1, 2]

for i, (x, y, p1, p2, h1, h2) in enumerate(zip(X, Y, P1, P2, H1, H2)):
    profit, corn, oats = farm_optimize(x, y, p1, p2, h1, h2)

    print(f"Optimized Acres for Test {i + 1}")
    print(f"Farm Acres: {x} acres, Farm Labor Hours: {y} hours")
    print(f"Corn: {corn} acres, Oats: {oats} acres")
    print(f"Optimized Profit: ${profit:,.0f}\n")
