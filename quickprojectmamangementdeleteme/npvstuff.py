# rate of return == discount rate


def is_project_viable(expenditure,cashyield,yearspan,discount_rate):
    print(f"Entered values:\nexpenditure -> {expenditure}\ncash yield -> {cashyield}\nyears -> {yearspan}\ndiscount "
          f"rate -> {discount_rate}")
    PV_of_benefits = cashyield/(1+(discount_rate/100))**yearspan
    return PV_of_benefits - expenditure


# x = is_project_viable(100000,200000,6,10)
# print(f"NPV -> {x}\n")


def npv_of_project(startupcost,listofrunningcosts,listofrevnues,saleofbusiness,discountrate):
    years = len(listofrevnues)
    discountrate_decimal = discountrate/100
    listofrunningcosts = [-y for y in listofrunningcosts]
    print(f"Entered discount rate: {discountrate} % -> {discountrate_decimal}\n"
          f"Start-up costs: {startupcost}")
    NPV = -startupcost
    for i in range(years):
        cashflow = listofrunningcosts[i] + listofrevnues[i]
        calc = cashflow / (1 + discountrate_decimal) ** (i + 1)
        if i == years-1: # last item
            cashflow += saleofbusiness
            calc = cashflow / (1 + discountrate_decimal) ** (i + 1)
            NPV += calc
        else:
            NPV += calc

    return NPV


# x = npv_of_project(50000,[30000,45000,45000],[40000,50000,60000],70000,12)
# print(x)
#
# x = npv_of_project(28000,[0,0,0],[8000,12000,17000],0,3)
# print(x)
#
# x = npv_of_project(50000,[30000,45000,45000],[40000,50000,60000],70000,12)
# print(x)

# future value == final value
def calculate_present_value(futurevalue,yearspan,discount_rate):
    return futurevalue/(1+(discount_rate/100))**yearspan


# x = calculate_present_value(2012,12,6)
# print("Present value is -> ", x)