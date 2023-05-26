class Employee:
    def __init__(self, name, salary, hours_per_week=40):
        self.name = name
        self._salary = salary
        self._hours_per_week = hours_per_week
        self.__set_hourly_rate()
    
    @property
    def hours_per_week(self):
        return self._hours_per_week
    
    @hours_per_week.setter
    def hours_per_week(self, value):
        self._hours_per_week = value
        self.__set_hourly_rate()
    
    @hours_per_week.deleter
    def hours_per_week(self):
        del self._hours_per_week
        
    @property
    def salary(self):
        return self._salary
    
    @hours_per_week.setter
    def hours_per_week(self, value):
        self._salary = value
        self.__set_hourly_rate()  
    
    @hours_per_week.deleter
    def hours_per_week(self):
        del self._salary
        
    @property
    def hourly_rate(self):
        return self._hourly_rate
    
    def __set_hourly_rate(self):
        self._hourly_rate = self._salary / 52 / self._hours_per_week


