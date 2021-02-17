from Models.database import Database
from Models.country import Country
from Views.page_view import PageView

class App:
    def __init__(self):
        # db_config
        local_host = 'localhost'
        default_port = '3306'
        test_user = 'testdev'
        user_pass = 'DevP@ssw0rd'
        auth_sha2 = 'caching_sha2_password'
        data_base = 'world'

        # connect with db_config
        self._cnx = Database.get_db_connection(
            host=local_host,
            port=default_port,
            user=test_user,
            password=user_pass,
            auth_plugin=auth_sha2,
            database=data_base)
        
        # Get cursor object
        self._search = self._cnx.cursor()

    def run(self):
        # App controller interface loop
        _running = True
        while _running:

            user_input = input("\nType '/q' to exit\n>>> SEARCH: ")
            if user_input == '/q':
                _running = False
                self._cnx.close()
                exit("Connection closed")
            else:
                try:
                    print("Searching...")
                    new_country = Country.constructor(self._search, user_input)
                    PageView.display_title(new_country.name)
                    PageView.display_country(new_country)
                    PageView.display_cities(new_country.major_cities)
                    
                except:
                    print(f">>> {user_input} did not match any entries")
