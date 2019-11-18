# file a03_1cm.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: functions for time value of money calculations

def future_value(r, n, pv):
    """Calculates, returns future value of a lump sum pv invested at r for n
    periods"""
    # formula for future value
    return pv * (1 + r) ** n

def present_value(r, n, fv):
    """Calculates +returns presnt value of lump sum fv discounted at r for n
    periods"""
    return fv / (1 + r) ** n

def present_value_of_annuity(r, n, pmt):
    """Calculates and returns present value of an annuity of  pmt to be received
    for n periods discounted at the rate r"""
    return (pmt * (1 - (1 + r)) ** -n) / r

def annuity_payment(r, n, pv):
    """Calculates the amortizing annuity payment for a present value of pv to
    be repaid at a periodic interest rate of r for n periods"""
    return (r * pv) / 1 - (1 + r) ** -n

def dollar_format(amount):
    """Creates formatted string representation of a numeric amount"""
    # create a string
    return "$" + str(int(amount))

def rate_of_return():
    return (int(0.03))
def life_cycle_model():
    # collect inputs for the rate of return, user's age, retirement age
    # and current income
    """Collect inputs and assign to variables"""
    return ("Enter the current inflation-indexed risk-free rate of return: " +
    str(rate_of_return))

def years_remaining():

    str(retirement_age) - str(user_age)
def financial_assets():

# example code
    if __name__ == '__main__' :
        life_cycle_model()

        print ("The payment amount is " + dollar_format(100))
        print ("Enter your age now: " + str(user_age))

        print ("Enter your expected retirement age: " + str(retirement_age))

        print ("Enter your current annual income: " + str(current_income))

        print ("Enter the value of your financial assets: " + financial_assets)

        print ("The present value of your human capital is $ ", present_value_of_annuity)
        print ("Your economic net worth is: ", str(financial_assets +
        present_value_of_annuity))
        print ("Your sustainable standard of living is about $64747 per year" )
        print ("You have", years_remaining, " remaining working years with an income of $ ",
        current_income, "per year")
        

