def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """

    masked_people = []
    for person in people:
        p_copy=person.copy()

        #MAskaa email
        if 'email' in p_copy and isinstance(p_copy['email'], str):
            email=p_copy['email']
            if email and '@' in email:
                local_part, domain =email.split('@',1)
                p_copy['email'] = '****'  + '@' + domain

        #Puhelinnumeron maskaus
        if 'phone' in p_copy and isinstance(p_copy['phone'], str):
            phone=p_copy['phone']
            if len(phone)>2:
                p_copy['phone'] = '*' * (len(phone) - 2) + phone[-2:]
            else:
                p_copy['phone']='**'

        masked_people.append(p_copy)
    
    return masked_people