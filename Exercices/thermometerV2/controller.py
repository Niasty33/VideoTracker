
class Controller:

    def __init__(self, model, view):

        self.__view = view
        self.__model = model
        self.__CELSIUS = "°C"
        self.__FAHRENHEIT = "°F"
        self.__KELVIN = "°K"

        #Binding
        self.__view.update(str(self.__model.getTemperature()) + self.__CELSIUS)

        #callback
        self.__view.increase_btn.config(command = self.increase)
        self.__view.decrease_btn.config(command = self.decrease)
        self.__view.farenheit_btn.config(command = self.farenheit)
        self.__view.celsius_btn.config(command = self.celsius)

    def increase(self) -> None:

        self.__model.increase()
        self.__view.update(str(self.__model.getTemperature()) + self.getUnit())

    def decrease(self) -> None:

        self.__model.decrease()
        self.__view.update(str(self.__model.getTemperature()) + self.getUnit())

    def fahrenheit(self) -> None:

        if self.getUnit() == self.__CELSIUS:
            self.__model.fahrenheit_from_celsius()
            self.__view.update(str(self.__model.getTemperature()) + self.__FAHRENHEIT)
        elif self.getUnit() == self.__KELVIN:
            self.__model.fahrenheit_from_kelvin()
            self.__view.update(str(self.__model.getTemperature()) + self.__FAHRENHEIT)
            
    def celsius(self):

        if self.getUnit() == self.__FAHRENHEIT:
            self.__model.celsius_from_fahrenheit()
            self.__view.update(str(self.__model.getTemperature()) + self.__CELSIUS)
        elif self.getUnit() == self.__KELVIN:
            self.__model.celsius_from_kelvin()
            self.__view.update(str(self.getTemperature()) + self.__CELSIUS)

    def kelvin(self):

        if self.getUnit() == self.__CELSIUS:
            self.__model.kelvin_from_celsius()
            self.__view.update(str(self.__model.getTemperature()) + self.__KELVIN)
        elif self.getUnit() == self.__FAHRENHEIT:
            self.__model.kelvin_from_fahrenheit()
            self.__view.update(str(self.getTemperature()) + self.__KELVIN)
            

    def getUnit(self) -> str:
        
        return self.__view.temperature_lbl['text'][-2:]