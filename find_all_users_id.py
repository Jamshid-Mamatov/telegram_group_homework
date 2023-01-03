from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    id_list=[]


    for user in data['messages']:
        if user.get('actor_id') is not None not in id_list:
            id_list.append(user.get('actor_id'))


    return id_list
data=read_data(file_path='data/result.json')

find_all_users_id(data=data)