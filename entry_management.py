# entry_management.py
from datetime import datetime, timedelta

class EntryManagement:
    def __init__(self):
        self.subscriptions = {}  # Abonelik bilgileri
        self.daily_entries = []  # Gunluk girisler

    def add_subscription(self, user_id, sub_type, duration_days):
        """Yeni abonelik ekle"""
        expiry_date = datetime.now() + timedelta(days=duration_days)
        self.subscriptions[user_id] = {
            "type": sub_type,
            "expiry": expiry_date,
            "active": True
        }
        print(f"{user_id} için {sub_type} abonelik eklendi. Bitis: {expiry_date}")

    def verify_qr_code(self, user_id):
        """QR kod ile doğrulama"""
        if user_id in self.subscriptions:
            sub = self.subscriptions[user_id]
            if sub["active"] and sub["expiry"] > datetime.now():
                print(f"{user_id} dogrulandi. Giris izni verildi.")
                return True
            else:
                print(f"{user_id} abonelik suresi dolmus veya aktif degil.")
                return False
        else:
            print(f"{user_id} abone degil.")
            return False

    def check_subscription_expiry(self):
        """Abonelik surelerini kontrol et ve uyari ver"""
        for user_id, sub in self.subscriptions.items():
            days_left = (sub["expiry"] - datetime.now()).days
            if days_left <= 3:
                print(f"Uyarı: {user_id} abonelik suresi {days_left} gun icinde dolacak!")

# Örnek kullanım
entry = EntryManagement()
entry.add_subscription("user123", "Abonman Kartli", 30)
entry.add_subscription("user456", "Gunluk Kart", 1)
entry.verify_qr_code("user123")
entry.check_subscription_expiry()