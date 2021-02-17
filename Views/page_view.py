class PageView:
    """
    Display view class
    """
    @staticmethod
    def display_title(results):
        print("\nWorld Factbook\n")
        print(results)
        print('='*24+'\n')


    @staticmethod
    def display_country(results):
        return results.__str__()

    
    @staticmethod
    def display_cities(results):
        print("List of major cities:")
        for result in results:
            print(F"- {result.name}, {result.country_code}")


    @staticmethod
    def display_data(search_results):
        print("Search results returned from the database:")
        print(search_results)
