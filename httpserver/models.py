from sqlalchemy.orm import relationship
from sqlalchemy import BigInteger, Column, Date, DateTime, ForeignKey, Integer, String, func
from .T_structure.database_table_structre import Base

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    name = Column(String(100), unique=True, unllable=False, comment='省')
    contury = Column(String(100), unique=True, unllable=False, comment='国家')
    contury_code = Column(String(100), unllable=False, comment='国家代码')
    contury_population = Column(BigInteger, unllable=False, comment='国家人口')
    #关联
    data = relationship("Data", back_populates="city")

    create_at= Column(DateTime, server_default=func.now(),comment='创建时间')
    updaed_at= Column(DateTime, server_default=func.now(),onupdate=func.now(),comment='更新时间')
    #安国家代码排序
    __mapper_args__ = {"order_by": contury_code}

    def __repr__(self):
        return f"City(name={self.name}_contury={self.contury}"
    
class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    #外键 类名. 属性名
    city_id = Column(Integer, ForeignKey("city.id"), comment='省')
    date = Column(Date, unllable=False, comment='数据日期')
    #city 类名关联
    city = relationship('City',back_populates='data')

    create_at= Column(DateTime, server_default=func.now(),comment='创建时间')
    updaed_at= Column(DateTime, server_default=func.now(),onupdate=func.now(),comment='更新时间')
    #安国家代码排序
    __mapper_args__ = {"order_by": date.desc()}

    def __repr__(self):
        return f"{repr(self.city)}:正确{self.date}"}"
