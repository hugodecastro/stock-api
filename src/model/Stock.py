from sqlalchemy import ARRAY, JSON, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from src.database import db


class Stock(db.Model):
    __tablename__: str = 'stock'

    id = Column(Integer, primary_key=True)
    status = Column(String(10), nullable=False)
    purchased_amount = Column(Integer, nullable=False)
    purchased_status = Column(String(20), nullable=False)
    request_data = Column(DateTime(timezone=True), server_default=func.now())
    company_code = Column(String(100), nullable=False)
    company_name = Column(String(100), nullable=False)
    stock_values = Column(JSON, nullable=False)
    performance_data = Column(JSON, nullable=False)
    competitors = Column(ARRAY, nullable=False)
    market_cap = Column(JSON, nullable=False)

    def __repr__(self) -> str:
        return f'<Stock {self.id}> has status {self.status}'
