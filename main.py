from models.transaction import Transaction
from models.category import Category

if __name__ == "__main__":
    food_cat = Category("Food", "Расходы на питание")
    salary_cat = Category("Salary", "Доходы от зарплаты")

    t1 = Transaction(100, food_cat.name, "2023-10-25", type_='expense')
    t2 = Transaction(5000, salary_cat.name, "2023-10-20", type_='income')

    print(food_cat)
    print(salary_cat)

    print(t1.formatted())
    print(t2.formatted())

    print("Food matches 'food':", food_cat.matches("food"))
    print("Food matches 'FOOD':", food_cat.matches("FOOD"))
    print("Food matches 'rent':", food_cat.matches("rent"))
