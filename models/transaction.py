# -finance-assistant-2026
class Transaction:
    """Класс для представления финансовой транзакции."""

    def __init__(self, amount, category, date, type_='expense'):
        """
        :param amount: сумма транзакции
        :param category: категория (строка)
        :param date: дата в формате YYYY-MM-DD
        :param type_: тип: 'income' или 'expense'
        """
        self.amount = amount
        self.category = category
        self.date = date
        self.type_ = type_

    def get_sign(self):
        """Возвращает знак суммы: + для дохода, - для расхода."""
        return 1 if self.type_ == 'income' else -1

    def formatted(self):
        sign = '+' if self.type_ == 'income' else '-'
        return f"{sign}{self.amount} ({self.category}, {self.date})"

    def __repr__(self):
        return f"Transaction({self.amount}, {self.category}, {self.date}, {self.type_})"
