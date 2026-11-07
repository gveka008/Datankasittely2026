def mask (users):
    #Mask phone  in data
    masked_users=[] 
    for user in users:
        u_copy = user.copy()
        if 'phone' in u_copy and isinstance(u_copy['phone'], str):
            phone=u_copy['phone']
            u_copy['phone']='*'*(len(phone)-2)+phone[-2:]
        masked_users.append(u_copy)
    return masked_users