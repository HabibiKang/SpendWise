import matplotlib.pyplot as plt

print("\nWelcome to SpendWise, your monthly budget buddy 💰\n")

income_names = []
income_amounts = []
expense_names = []
expense_amounts = []

def main():
    while True:
        try:
            inc_or_ex = str(input("\nType 'I' to add an income, type 'E' to enter an expense,\nor 'C' to calculate budget ratio.\n")).title()
            if inc_or_ex == "I":
                income()
                break
            elif inc_or_ex == "E":
                expense()
                break
            elif inc_or_ex == "C":
                calculate()
                break
        except ValueError:
            print("Invalid Entry, please try again.")
            continue

def income():
    while True:
        try:
            income_name = str(input("Income Source: "))
            income_names.append(income_name)
            income_amount = int(input(f"Income Amount for {income_name}: "))
            income_amounts.append(income_amount)
            main()
        except ValueError:
            print("Invalid Entry, please try again.")
            continue

def expense():
    while True:
        try:
            expense_name = str(input("Expense Source: "))
            expense_names.append(expense_name)
            expense_amount = int(input(f"Expense Amount for {expense_name}: "))
            expense_amounts.append(expense_amount)
            main()
        except ValueError:
            print("Invalid Entry, please try again.")
            continue

def calculate():
    make_dict = {}
    for i in range(len(income_names)):
        make_dict[income_names[i]] = income_amounts[i]
    for i in range(len(expense_names)):
        make_dict[expense_names[i]] = expense_amounts[i]
    
    y = income_amounts + expense_amounts
    mylabels = income_names + expense_names

    total_income = sum(income_amounts)
    total_expenses = sum(expense_amounts)
    ratio = total_income - total_expenses

    colors = ['green'] * len(income_amounts) + ['red'] * len(expense_amounts)

    plt.pie(y, labels=mylabels, colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    plt.legend(title="Budget Ratio", labels=make_dict.items(), loc="lower left", bbox_to_anchor=(-0.4, -0.15))
    text_content = f"This June, you earned ${total_income}\nand spent ${total_expenses} this month.\nYour budget ratio is ${ratio}."
    plt.text(1.5, -1.6, text_content, fontsize=12, color='black', ha='right', va='bottom', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))
    plt.show()

if __name__ == "__main__":
    main()
