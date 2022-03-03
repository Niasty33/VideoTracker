class Model:

    def __init__(self, temperature : int):
        
        self.__temperature = temperature

    def increase(self) -> int:
        
        self.__temperature += 1

    def decrease(self) -> int:

        self.__temperature -= 1

    def celsius_from_fahrenheit(self) -> int:
        
        self.__temperature = int((self.__temperature - 32) * 5 / 9)

    def celsius_from_kelvin(self) -> int:

        self.__temperature = int(self.__temperature - 273,15)

    def farenheit_from_celsius(self) -> int:
        
        self.__temperature =  int(9 / 5 * self.__temperature + 32)

    def fahrenheit_from_kelvin(self) -> int:

        self.__temperature = (self.__temperature - 273,15) * 9/5 + 32
    
    def kelvin_from_celsius(self) -> int:

        self.__temperature = int(self.__temperature + 273,15)
    
    def kelvin_from_fahrenheit(self) -> int:

        self.__temperature = int((self.__temperature - 32) * 5/9 + 273,15)


    def getTemperature(self) -> int:
        
        return self.__temperature