from pydantic import BaseModel, Field, validator
from dto.itemorigin import ItemOrigin

class InventoryItem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin