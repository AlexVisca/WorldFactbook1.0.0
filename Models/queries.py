class SQL:
    """ Common SQL queries

    Returns:
        tuple: tuple containing row data
    """
    @staticmethod
    def select_id(cursor, search_term):
        query = "SELECT * FROM country where code = %s;"
        cursor.execute(query, (search_term,))
        result = cursor.fetchall()
        # result is a list with only one tuple
        return result[0]

    @staticmethod
    def select_country(cursor, country):
        # Select country
        query = "SELECT * FROM country WHERE Name = %s;"
        cursor.execute(query, (country,))
        result = cursor.fetchall()
        # result is a list with only one tuple
        return result[0]

    @staticmethod
    def select_cities(cursor, country_code):
        # Select all cities matching country code
        query = "SELECT * FROM city WHERE CountryCode = %s;"
        cursor.execute(query, (country_code,))
        result = cursor.fetchall()
        # result is a list with tuples
        return result

    @staticmethod
    def select_capital_city(cursor, capital_id):
        # Select the city matching the capital city id
        query = "SELECT * FROM city WHERE ID = %s;"
        cursor.execute(query, (capital_id,))
        result = cursor.fetchall()
        # result is a list with only one tuple, name of city at position [1]
        return result[0][1]

