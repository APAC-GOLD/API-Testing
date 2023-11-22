from dto.itemorigin import ItemOrigin
from dto.inventoryitem import InventoryItem
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()


my_inventory_item_dict: Dict[str, InventoryItem] = {}


@app.put("/items/{serial_num}")
def create_item(item: InventoryItem, serial_num: str) -> None:
    my_inventory_item_dict[serial_num] = item
    print(my_inventory_item_dict)



# Get API Test - if serial number is not given then this is the "Get-All-API"
@app.get("/items/{serial_num}")
def get_item(serial_num: str) -> InventoryItem:
    if serial_num is None: # Another check for if the serial number is not given
        print(my_inventory_item_dict.values())
        return list(my_inventory_item_dict.values())
    else:
        if serial_num in my_inventory_item_dict.keys():
            return my_inventory_item_dict[serial_num]
        else:
            raise HTTPException(status_code=404, detail="Item not found:" + serial_num)


# Delete Test
@app.delete("/items/{serial_num}")
def delete_item(serial_num: str) -> Dict:
    if serial_num in my_inventory_item_dict.keys():
        my_inventory_item_dict.pop(serial_num)
        print(my_inventory_item_dict)
        return {"msg": "Successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Item not found : " + serial_num)


@app.get("/items/")
def get_items() -> List[InventoryItem]:
    return my_inventory_item_dict.values()
