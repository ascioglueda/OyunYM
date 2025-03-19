# main.py
from entry_management import EntryManagement
from game_area import GameArea
from staff_management import StaffManagement
from reporting import Reporting
from density_prediction import DensityPrediction
from accounting import Accounting

def main():
    print("=== Oyun Alani Yonetim Sistemi ===")
    
    # Modülleri başlat
    entry = EntryManagement()
    game_area = GameArea()
    staff = StaffManagement()
    report = Reporting()
    density = DensityPrediction()
    accounting = Accounting()

    # Örnek işlemler
    entry.add_subscription("user123", "Abonman Kartli", 30)
    game_area.record_ride("user123", 15, 5)
    staff.add_staff("staff001", "Eda", 5000)
    report.add_sale(1000)
    density.add_historical_data("2025-03-19", 60)
    accounting.add_revenue(5000)

    # Raporlar
    report.generate_daily_report()
    density.predict_density("2025-03-20")
    accounting.generate_financial_report()

if __name__ == "__main__":
    main()