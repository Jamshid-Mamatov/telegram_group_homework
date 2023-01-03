from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    name_list=[]
    for message in data['messages']:
        if message.get('actor') is not None not in name_list:
            name_list.append(message.get('actor'))

    return name_list
find_all_users_name(data=read_data(file_path='data/result.json'))