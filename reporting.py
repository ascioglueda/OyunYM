# reporting.py
class Reporting:
    def __init__(self):
        self.subscriptions = []  # Abonelik kayıtları
        self.cancellations = []  # İptaller
        self.sales = []  # Satışlar
        self.programs = []  # Programlar (okul, grup)

    def add_subscription(self, user_id, sub_type):
        self.subscriptions.append((user_id, sub_type))
        print(f"{user_id} abonelik eklendi: {sub_type}")

    def add_cancellation(self, user_id):
        self.cancellations.append(user_id)
        print(f"{user_id} abonelik iptal edildi.")

    def add_sale(self, amount):
        self.sales.append(amount)
        print(f"Satis eklendi: {amount}")

    def add_program(self, program_type, count):
        self.programs.append((program_type, count))
        print(f"Program eklendi: {program_type}, {count} kişi")

    def generate_daily_report(self):
        """Gunluk rapor olustur"""
        print("=== Gunluk Rapor ===")
        print(f"Toplam Abonelik: {len(self.subscriptions)}")
        print(f"Iptaller: {len(self.cancellations)}")
        print(f"Toplam Satis: {sum(self.sales)}")
        print(f"Programlar: {self.programs}")

# Örnek kullanım
report = Reporting()
report.add_subscription("user123", "Abonman Kartli")
report.add_cancellation("user456")
report.add_sale(1000)
report.add_program("Okul", 30)
report.generate_daily_report()