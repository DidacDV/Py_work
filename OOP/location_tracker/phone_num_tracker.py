import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
class Phone:
    def __init__(self, number, location  = "", service = "") -> None:
        try:
            number = phonenumbers.parse(number)
            self.number = number
            self.location = service
            self.service = location
        except:
            raise ValueError("Insert valid number")
        
    def get_info(self, number, language):
        self.location = geocoder.description_for_number(number, language)
        self.service = carrier.name_for_number(number, language)
        
    
    def __str__(self):
        return(f"{self.number}\nLocation = {self.location}\nService = {self.service}")

    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, number):
        self._number = number
    
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, location):
        self._location = location

    @property
    def service(self):
        return self._service
    @service.setter
    def service(self, service):
        self._service = service
