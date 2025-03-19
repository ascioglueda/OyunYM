# density_prediction.py
class DensityPrediction:
    def __init__(self):
        self.historical_data = []  

    def add_historical_data(self, date, occupancy):
        self.historical_data.append((date, occupancy))

    def predict_density(self, date):
        """Basit bir yogunluk tahmini (ortalama)"""
        if not self.historical_data:
            return 0
        avg_occupancy = sum(data[1] for data in self.historical_data) / len(self.historical_data)
        print(f"{date} icin tahmini yogunluk: {avg_occupancy:.2f}%")
        return avg_occupancy

# Örnek kullanım
density = DensityPrediction()
density.add_historical_data("2025-03-18", 40)
density.add_historical_data("2025-03-19", 60)
density.predict_density("2025-03-20")