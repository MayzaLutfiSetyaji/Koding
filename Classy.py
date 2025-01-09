class Mountain:
#Konstruktor
    def __init__(self, name = "", region = "", elevation = 0):
        self.name = name
        self.region = region
        self.elevation = elevation
#Perilaku
    def info(self):
        print(f"Nama Gunung:{self.name}")
        print(f"Region:{self.region}")
        print(f"Ketinggian:{self.elevation}m")
        print()

#Objek dan atribut
mountain_1 = Mountain("Gunung Everest", "Asia", 8848)
mountain_1.info()
mountain_1.info()

mountain_2 = Mountain("Gunung Kilimanjaro", "Afrika")
mountain_2.elevation = 5895

mountain_3 = Mountain(name="Gunung Aconcagua", elevation=6961)
mountain_3.region = "Amerika Selatan"
mountain_3.info()

mountain_4 = Mountain()
mountain_4.name = "Gunung Kosciuszko"
mountain_4.region = "Australia"
mountain_4.elevation = 2228
mountain_4.info()

