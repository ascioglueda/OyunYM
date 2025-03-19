# staff_management.py
class StaffManagement:
    def __init__(self):
        self.staff = {}  # Personel bilgileri
        self.schedule = {}  # Nöbet çizelgesi

    def add_staff(self, staff_id, name, salary):
        """Yeni personel ekle"""
        self.staff[staff_id] = {"name": name, "salary": salary, "leaves": 0}
        print(f"{name} (ID: {staff_id}) eklendi. Maas: {salary}")

    def assign_shift(self, staff_id, date, shift):
        """Nobet cizelgesine ekle"""
        if staff_id in self.staff:
            self.schedule[(staff_id, date)] = shift
            print(f"{staff_id} icin {date} tarihinde {shift} nobeti eklendi.")
        else:
            print(f"{staff_id} bulunamadi.")

    def record_leave(self, staff_id, days):
        """İzin kaydı"""
        if staff_id in self.staff:
            self.staff[staff_id]["leaves"] += days
            print(f"{staff_id} için {days} gun izin kaydedildi.")
        else:
            print(f"{staff_id} bulunamadi.")

# Örnek kullanım
staff = StaffManagement()
staff.add_staff("staff001", "Eda", 5000)
staff.assign_shift("staff001", "2025-03-20", "Morning")
staff.record_leave("staff001", 2)