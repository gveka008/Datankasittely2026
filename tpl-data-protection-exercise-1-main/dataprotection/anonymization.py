from datetime import datetime

def anonymize(people):
    """
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """

    anonymized_people = []
    for person in people:
        p_copy=person.copy()
       
        #nimen poisto
        if 'name' in p_copy:
            del p_copy['name']

        #Vain syntymävuosi
        if 'birthdate' in p_copy:
            birth_val=p_copy['birthdate']
            #Len tarkistaa teksti pituuden ja isinstance tarkistaa tyypi
            if isinstance(birth_val, str) and len(birth_val)>=4:
                p_copy['birth_year']=int (birth_val[:4])
            del p_copy['birthdate']

        #Vain kaupungin eka kirjain
        if 'city' in p_copy and isinstance(p_copy['city'],str) and len(p_copy['city'])>0:
            p_copy['city_initial']=p_copy['city'][0]
            del p_copy['city']

        anonymized_people.append(p_copy)

    return anonymized_people