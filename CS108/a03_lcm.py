# file: a03_lcm.py
# author: Sofia Kurd (sofiak@bu.edu)
# description: Life-cycle model of saving and consumption

from a03_tvm import present_value_of_annuity
from a03_tvm import annuity_payment
from a03_tvm import dollar_format

def life_cycle_model():
    """Finds smooth level of consumption"""
    rate_of_return = 0.03
    user_age = 32
    retirement_age = 65
    current_income = 89000
    financial_assets = 100000

    remaining_working_years = (retirement_age - user_age)
    print (int(remaining_working_years))
    human_capital = (remaining_working_years * current_income)
    print (int(human_capital))
    economic_net_worth = (human_capital + financial_assets)
    print (int(economic_net_worth))
    sustainable_living_standard = annuity_payment + (str(100)) - retirement_age
    print (int(sustainable_living_standard))
    annual_savings = current_income - sustainable_living_standard
    print (int(annual_savings))

if __name__ == '__main__':

    life_cycle_model()

    
