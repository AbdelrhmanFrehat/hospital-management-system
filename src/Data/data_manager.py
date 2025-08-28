import json
import os.path
from typing import List, Optional

from src.Data.idata_manager import IDataManager, T


class DataManger(IDataManager[T]):

    def __init__(self,filename:str, id_field:str='id'):
         self.filename=filename
         self.id_field=id_field
         self.data=self.load_data()

    def load_data(self) -> List[T]:
        try:
            if os.path.exists(self.filename):
                with open(self.filename,'r',encoding='utf-8')as file:
                    return json.load(file)
            return[]
        except (FileNotFoundError,json.JSONDecodeError):
            return []

    def save_data(self,data:List[T]) -> None:
        try:
            with open(self.filename,'w',encoding='utf-8')as file:
                json.dump(data,file,ensure_ascii=False,indent=4)
        except Exception as e:
            raise  Exception(e)

    def get_all(self) -> List[T]:
        return self.data.copy()

    def get_by_id(self,id) -> Optional[T]:
        for item in self.data:
            if item.get(self.id_field)==id:
                return item
        return None

    def add(self, item:T) -> None:
        if not isinstance(item,dict):
            raise ValueError("the item must be dict")

        if self.id_field not in item:
            raise ValueError("the item must have an id")

        new_id = item[self.id_field]

        if any(existing.get(self.id_field) == new_id for existing in self.data):
            raise ValueError("id is already used")

        self.data.append(item)
        self.save_data(self.data)

    def update(self, item_id: str, **kwargs) -> Optional[T]:
        for item in self.data:
            if item.get(self.id_field)==item_id:
                for key,value in kwargs.items():
                    if key != self.id_field:
                        item[key]=value
                self.save_data(self.data)
                return item
            return None

    def delete(self,id) -> bool:
        for i, item in enumerate(self.data):
            if item.get(self.id_field)==id:
                del self.data[i]
                self.save_data(self.data)
                return True
        return False