from Models.queries import SQL
from Models.city import City

class Country:
    """
    Initialises a Country object
    """
    def __init__(self, code_, name_, continent_, region_, surface_area_, \
    indep_year_, population_, life_expect_, gnp_, gnp_old, local_name_, \
    gov_form_, head_of_state_, capital_id, code_2_):
        self._code = code_
        self._name = name_
        self._continent = continent_
        self._region = region_
        self._surface_area = surface_area_
        self._indep_year = indep_year_
        self._population = population_
        self._life_expectancy = life_expect_
        self._GNP = gnp_
        self._GNP_old = gnp_old
        self._local_name = local_name_
        self._government = gov_form_
        self._head_of_state = head_of_state_
        self._capital_id = capital_id
        self._code_2 = code_2_
        self._capital_city = None
        self._cities = None

    def __str__(self):
        print(F"Country name: {self._name}\nCountry code: {self._code}\n\nCapital city: {self._capital_city}")
    
    @property
    def name(self):
        return self._name

    @property
    def country_code(self):
        return self._code

    @property
    def capital_id(self):
        return self._capital_id

    @property
    def capital_city(self):
        return self._capital_city
    
    @property
    def major_cities(self):
        return self._cities
    
    @classmethod
    def constructor(cls, search, user_input):
        # print(F"Searching for {user_input} in the database...")
        _CONFIG = SQL.select_country(search, user_input)
        # print(F"Found {user_input}")
        canada = Country(*_CONFIG)
        can_id = canada.country_code
        # print("Identifying capital city")
        ott_id = canada.capital_id
        ottawa = SQL.select_capital_city(search, ott_id)
        canada._capital_city = ottawa
        # print("Creating list of major cities")
        cities_list = SQL.select_cities(search, can_id)
        list_of_cities = City.constructor(cities_list)
        canada._cities = list_of_cities
        # print("Complete")
        return canada
