# file: a03_lcm.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: Life-cycle model of saving and consumption
from a03_tvm import present_value_of_annuity
from a03_tvm import annuity_payment
from a03_tvm import dollar_format

def life_cycle_model()
    print "Enter the current inflation-indexed risk-free rate of return:", int(0.03)
    print "Enter your age now:",  int(35)
    print "Enter your expected retirement age:", int(67)
    print "Enter your current annual income:", int(83000)
    print "You have" + int(32), "remaining working years with an income of $ "
    int(83000), "per year."
    print "The present value of your human capital is about $", int(1692267)
    print "Enter the value of your financial assets:", int(150000)
    print "Your economic net worth is:", int(1842267)

if __name__ == '__main__':

    life_cycle_model()
