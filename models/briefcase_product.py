from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey

class BriefcaseProductModel(Base):
    __tablename__ = 'briefcase_product'
    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True),
    briefcase_id = Column(Integer, ForeignKey("briefcase.id"), primary_key=True),
