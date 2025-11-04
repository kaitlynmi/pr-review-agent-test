def divide(a, b):
       return a / b
   
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

def read_file(path):
    f = open(path)
    return f.read()