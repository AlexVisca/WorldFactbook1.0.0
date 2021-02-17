class City:
    """
    Initialises a City object
    """
    def __init__(self, id_, name_, country_code_, district_, population_):
        self._id = id_
        self._name = name_
        self._country_code = country_code_
        self._district = district_
        self._population = population_
    
    def __str__(self):
        print(F"- {self._name}, {self._country_code}")

    @property
    def name(self):
        return self._name

    @property
    def country_code(self):
        return self._country_code

    @classmethod
    def constructor(cls, list_of_cities):
        major_cities = list()
        for city in list_of_cities:
            one_city = City(*city)
            major_cities.append(one_city)
        return major_cities
