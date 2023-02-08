from models.user import User as UserModel

class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self, id):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not result:
            result = {"message": "User not found"}
            return result
        return result


    def create_user(self, user) -> None:
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()

    def update_user(self, id, user) -> dict:
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not result:
            result={"message": "user not found"}
            return result
        result.first_name = user.first_name
        result.last_name = user.last_name
        result.dni = user.dni
        result.email = user.email
        result.password = user.password
        result.state = user.state
        # seve data
        self.db.commit()
        return {"message": "user update with success"}

    def delete_user(self, id) -> dict:
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        if not result:
            result = {"message": "user not found"}
            return result
        
        # self.db.delete(result)
        # aqui decidi solo cambiar el state (1 - activo, 0 - inactivo)
        result.state = 0
        self.db.commit()
        return {"message": "user dado de baja con exito"}
        