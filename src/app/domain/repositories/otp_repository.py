from typing import Protocol, Self
from abc import abstractmethod

from app.domain.entities.otp_entity import OtpEntity
from app.domain.value_objects.action_uuid_value_object import ActionUUID


class OtpRepositoryInterface(Protocol):
    @abstractmethod
    async def create_otp(self: Self) -> OtpEntity:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def get_otp_by_action_uuid(self: Self, action_uuid: ActionUUID) -> OtpEntity:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def remove_otp_by_action_uuid(self: Self, action_uuid: ActionUUID) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )