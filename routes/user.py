from fastapi import APIRouter, Depends
from models.user import User

router = APIRouter()


users = [
    User(name="Nareeya" , id= 1),
    User(name="fana" , id = 2)
]

@router.get("/api/v1/users")
def get_user () : 
    return users


@router.post("/api/v1/users")
def create_user(user: User):
    for existing_user in users:
        if existing_user.name == user.name:
            return f"User with name {user.name} already exists"

    # Find the user with the maximum id
    max_id = max(users, key=lambda user: user.id, default=0).id


    # Create a new user with the generated ID
    new_user = User(name=user.name, id=max_id + 1)

    # Append the new user to the list
    users.append(new_user)

    return users

@router.delete("/api/v1/users/{id}")
def delete_user (id) :
   user = next((user for user in users if user.id == id), None)

   if user == None :
       return f"User with id {id} does not exist"
   
   users.remove(user)
   return "remove user successfully"



