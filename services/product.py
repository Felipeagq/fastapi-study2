from models.user import Product as ProductModel

class ProductService():

    def __init__(self, db) -> None:
        self.db = db

    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result

    def get_product(self, id):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        if not result:
            result = {"message": "product not found"}
            return result
        return result


    def create_product(self, product) -> None:
        new_product = ProductModel(**product.dict())
        self.db.add(new_product)
        self.db.commit()

    def update_product(self, id, product) -> dict:
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        if not result:
            result={"message": "product not found"}
            return result
        result.name = product.name
        result.image = product.image
        result.tipo = product.tipo
        result.state = product.state
        # seve data
        self.db.commit()
        return {"message": "product update with success"}

    def delete_product(self, id) -> dict:
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        if not result:
            result = {"message": "product not found"}
            return result
        
        # self.db.delete(result)
        # aqui decidi solo cambiar el state (1 - activo, 0 - inactivo)
        result.state = 0
        self.db.commit()
        return {"message": "producto dado de baja con exito"}