def taxes(income):
    """Calculation of taxes to be paid for a taxable income x"""
    if income <= 8004:
        tax = 0
    elif income <= 13469:
        y = (income -8004.0)/10000.0
        tax = (912.17 * y + 1400)*y
    elif income <= 52881:
        z = (income -13469.0)/10000.0
        tax = (228.74 * z +2397.0)*z +1038.0
    elif income <= 250730:
        tax = income * 0.42 - 8172.0
    else:
        tax = income * 0.44 - 15694
    return tax

x = taxes(123456)
print x
