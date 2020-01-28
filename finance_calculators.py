# -------------------------------- START OF CODE! -----------------------------------------
# TITLE: Finance_Calculators
# AIM: Assist user to calculate interest.
# AUTHOR: Rishen Gopaldass
# -----------------------------------------------------------------------------------------

def main():

    import math

    # This is an instruction to the user.
    # Skip a line.
    print("Choose either 'Investment' or 'Bond' from the menu below to proceed:")
    print()

    # This is a display of an option to the user.
    # This is a display of an option to the user.
    # Skip a line.
    print(" Investment \t" + "- to calculate the amount of interest you wil earn on interest.")
    print(" Bond       \t" + "- to calculate the amount you will have to pay on a home loan.")
    print()


    # Obtaining user's choice of calculation here
    UserChoice = input("Please type in your selection here: ")

   

    # Running the investment calculation:
    # Variables described.
    # Equation for calculation purposes.
    if UserChoice == "Investment" or UserChoice == "investment" or UserChoice == "INVESTMENT" or UserChoice == "iNVESTMENT":
        InvestPV = float(input("Please enter the investment amonunt of your choice: "))
        InvestRate = float(input("Please enter the interest rate: "))
        InvestPeriod = float(input("Please enter the period: "))
        InvestType = input("Please enter your investment interest type. (Simple or Compound): ")

        InvestSimple = InvestPV * (1+(InvestRate/100)*InvestPeriod)
        InvestCompound = InvestPV*math.pow((1+(InvestRate/100)),InvestPeriod)

        if InvestType == "Simple" or InvestType == "simple" or InvestType == "SIMPLE" or InvestType == "sIMPLE":
            print("R " + str(InvestSimple))
        elif InvestType == "Compound" or InvestType == "compound" or InvestType == "COMPOUND" or InvestType == "cOMPOUND":
            print("R " + str(InvestCompound))
        else:
            print()
            print("ERROR2 !!! Please type in (Simple or Compound)! ")
            main()


    # Running the bond Calculation:
    # Variables described.
    # Equation for calculation purposes.
    elif UserChoice == "Bond" or UserChoice == "bond" or UserChoice == "BOND" or UserChoice == "bOND":
        BondPV = float(input("Please enter the present value of your house: "))
        BondRate = float(input("Please enter the rate: "))
        BondPeriod = float(input("Please enter the payment period of your choice: "))
        BondRepayment = BondPV / ((1-(1-(BondRate/100))*BondPeriod) * BondRate)
        print("R " + str(BondRepayment) + " per month.")


    # Returning user back to making their choice of calculation:
    else:
        print()
        print("ERROR1 !!! Your choice did not match the options provided. Please try again!")
        main()

main()


# -------------------------------- END OF CODE! -----------------------------------------