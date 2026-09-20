class Category:
    """Класс категории для транзакций."""

    def __init__(self, name, description=""):
        """
        :param name: название категории (например, 'Food')
        :param description: описание категории
        """
        self.name = name
        self.description = description

    def matches(self, text: str) -> bool:
        """Проверяет, совпадает ли текст с названием категории (регистронезависимо)."""
        return text.lower() == self.name.lower()

    def __repr__(self):
        return f"Category({self.name}, {self.description})"
