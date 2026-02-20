user_rename = {}

async def set_rename(user_id, name):
    user_rename[user_id] = name

def get_rename(user_id):
    return user_rename.get(user_id)
