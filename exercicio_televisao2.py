#Maneira 2
def main():
    class Televisao:
        def __init__(self, marca):
            self.marca = marca
            self.volume = 0

        def aumentarVolume(self):
            if self.volume < 10:
                self.volume = self.volume + 1
                print("Volume atual: " + str(self.volume))
            else:
                print("A televisão está no volume máximo!")

        def diminuirVolume(self):
            if self.volume > 0:
                self.volume = self.volume - 1
                print("Volume atual: " + str(self.volume))
            else:
                print("A televisão está zerado!")

    tv_nova = Televisao("Samsung")
    tv_nova.aumentarVolume()
    tv_nova.diminuirVolume()

main()