from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    count=0
    all_id=find_all_users_id(data=data)
    for message in data['messages']:
        
        if users_id in all_id:
            
            if (message.get('from_id') is not None )and message.get('from_id')== users_id:
                count+=1
    print(count)
    return count
data=read_data(file_path="data/result.json")
user_id='user985722002'
find_user_message_count(data=data,users_id=user_id)
