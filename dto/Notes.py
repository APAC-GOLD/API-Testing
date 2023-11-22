from dto.itemorigin import ItemOrigin
from dto.inventoryitem import InventoryItem

from pydantic import BaseModel, Field, validator

my_inventoryitem1 = InventoryItem(name = "Homer Simpson",
                                  quantity = 1, 
                                  serial_num = "simpsons",
                                  origin= ItemOrigin(country="Ethiopia", production_date= "2021"))
my_inventoryitem2 = InventoryItem(name = "Ren and Stimpy", 
                                  quantity= 2,
                                  serial_num = "nickalodeon",
                                  origin= ItemOrigin(country="Ethiopia", production_date="2022"))
my_inventoryitem3 = InventoryItem(name= "Candyland", 
                                  serial_num = "jaffa",
                                  quantity= 3, 
                                  origin= ItemOrigin(country="Ethiopia", production_date="2023"))
#dictionary
my_iventory_items_dict = {"item1": my_inventoryitem1, "item2": my_inventoryitem2, "item3": my_inventoryitem3}

@app.get("/items/{item_id}")
def read_item(item_id: int, item: Item, q: Union[str, None] = None): #Default value for q is None
    return {"item_id": item_id, "q": q, "item": item}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}

#to get the item 3 from the dict:
item3_to_get = my_iventory_items_dict["item3"]

@validator("country")
def check_valid_country(cls, country: str):
        assert country == "Ethiopia", "country name must be Ethiopia"
        return country

class inventoryitem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin

def main():
    item_origin = ItemOrigin(country="Ethiopia", production_date="02/12/2023")
    my_item1 = inventoryitem(name="printer",
                             quantity=5,
                             serial_num="hdouhkjn",
                             origin=item_origin)
    my_serialized_object1 = my_item1.dict()
    print(my_serialized_object1)
    my_item2 = inventoryitem(**my_serialized_object1)
    print(my_item2.dict())

if __name__ == "__main__":
    main()



def main():
    item_origin = ItemOrigin(country = "Ethiopia", production_date = "02/12/2023")
    my_item1 = InventoryItem(name = "printer",
                             quantity = 5,
                             serial_num = "HDOUHKJN",
                             origin = item_origin)
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1)
    my_item2 = InventoryItem(**my_serialized_object1)
    print(my_item2.__dict__)

if __name__ == "__main__":
    main()



__________________________________________
from pydantic import BaseModel, field_validator


class ItemOrigin(BaseModel):
    country: str
    production_date: str

    @field_validator("country")
    @classmethod
    def check_valid_country(cls, country: str):
        assert country == "Ethiopia", "country name must be Ethiopia"
        return country

class InventoryItem(BaseModel):
    name: str
    quantity: int
    serial_num: str
    origin: ItemOrigin


def main():
    item_origin = ItemOrigin(country = "Ethiopia", production_date = "02/12/2023")
    my_item1 = InventoryItem(name = "printer",
                             quantity = 5,
                             serial_num = "HDOUHKJN",
                             origin = item_origin)
    my_serialized_object1 = my_item1.__dict__
    print(my_serialized_object1)
    my_item2 = InventoryItem(**my_serialized_object1)
    print(my_item2.__dict__)

if __name__ == "__main__":
    main()



OUTPUT
{'name': 'printer', 'quantity': 5, 'serial_num': 'hdouhkjn', 'origin': {'country': 'ethiopia', 'production_date': '02/12/2023'}}
{'name': 'printer', 'quantity': 5, 'serial_num': 'HDOUHKJN', 'origin': ItemOrigin(country='Ethiopia', production_date='02/12/2023')}
{'name': 'printer', 'quantity': 5, 'serial_num': 'HDOUHKJN', 'origin': ItemOrigin(country='Ethiopia', production_date='02/12/2023')}