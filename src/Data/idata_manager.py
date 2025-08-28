from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

T= TypeVar('T')

class IDataManager(ABC,Generic[T]):

    @abstractmethod
    def load_data(self) -> List[T]:
        pass

    @abstractmethod
    def save_data(self,data:List[T]) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def get_by_id(self,id) -> Optional[T]:
        pass

    @abstractmethod
    def add(self, item:T) -> None:
        pass

    @abstractmethod
    def delete(self,id) -> bool:
        pass

    @abstractmethod
    def update(self, item_id: str, **kwargs) -> Optional[T]:
        pass
