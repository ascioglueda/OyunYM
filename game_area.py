# game_area.py
class GameArea:
    def __init__(self):
        self.rides = []  # Biniş verileri
        self.metrics = {"noise": 0, "occupancy": 0, "electricity": 0, "temperature": 0}

    def record_ride(self, user_id, age, duration):
        """Binis verisini kaydet"""
        settings = self.customize_by_age(age)
        self.rides.append({
            "user_id": user_id,
            "age": age,
            "duration": duration,
            "settings": settings
        })
        print(f"{user_id} icin binis kaydedildi: {settings}")

    def customize_by_age(self, age):
        """Yas profiline göre ozellestirme"""
        if age < 10:
            return {"speed": "low", "music": "soft", "duration": "short"}
        elif 10 <= age <= 18:
            return {"speed": "medium", "music": "pop", "duration": "medium"}
        else:
            return {"speed": "high", "music": "rock", "duration": "long"}

    def update_metrics(self, noise, occupancy, electricity, temperature):
        """Veri ölçümlerini güncelle"""
        self.metrics["noise"] = noise
        self.metrics["occupancy"] = occupancy
        self.metrics["electricity"] = electricity
        self.metrics["temperature"] = temperature
        print(f"Veriler güncellendi: {self.metrics}")

# Örnek kullanım
game_area = GameArea()
game_area.record_ride("user123", 15, 5)
game_area.update_metrics(noise=70, occupancy=50, electricity=200, temperature=25)