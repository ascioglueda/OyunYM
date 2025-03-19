# accounting.py
class Accounting:
    def __init__(self):
        self.expenses = []  # Harcamalar
        self.revenues = []  # Gelirler

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))
        print(f"Harcama eklendi: {description}, {amount}")

    def add_revenue(self, amount):
        self.revenues.append(amount)
        print(f"Gelir eklendi: {amount}")

    def generate_financial_report(self):
        """Kar/Zarar raporu oluştur"""
        total_revenue = sum(self.revenues)
        total_expense = sum(expense[0] for expense in self.expenses)
        profit_loss = total_revenue - total_expense
        print("=== Finansal Rapor ===")
        print(f"Toplam Gelir: {total_revenue}")
        print(f"Toplam Gider: {total_expense}")
        print(f"Kar/Zarar: {profit_loss}")

# Örnek kullanım
accounting = Accounting()
accounting.add_expense(2000, "Elektrik Faturasi")
accounting.add_revenue(5000)
accounting.generate_financial_report()