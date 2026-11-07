def anonymize (users):
    #Anonymize name in data
    anonymized_users=[] 
    for user in users:
        u_copy = user.copy()
        if 'name' in u_copy and isinstance(u_copy['name'], str):
            u_copy['name']=u_copy['name'][0]
        anonymized_users.append(u_copy)
    return anonymized_users 