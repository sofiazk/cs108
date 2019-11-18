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
    return pmt * (1 - ((1 + r) ** -n)) / r

def annuity_payment(r, n, pv):
    """Calculates the amortizing annuity payment for a present value of pv to
    be repaid at a periodic interest rate of r for n periods"""
    return (r * pv) / (1 - ((1 + r) ** -n))

def dollar_format(amount):
    """Creates formatted string representation of a numeric amount"""
    # create a string
    return "$" + str(int(amount))

# test code
if __name__ == '__main__' :
    print ("The payment amount is " + dollar_format(100))
pv = present_value
fv = future_value
pmt = present_value_of_annuity
