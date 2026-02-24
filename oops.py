class Computer:
    def __init__(self , cpu , ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print(f"Config is {self.cpu} and {self.ram}")

comp1 = Computer('i5' , 16)
comp2 = Computer('i7' , 32)
Computer.config(comp1)
Computer.config(comp2)