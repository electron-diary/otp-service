from typing import Self
from dataclasses import dataclass
from uuid import UUID

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class Otp(DomainValueObject[int]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "Otp cannot be empty"
            )
        if not isinstance(self.object, int):
            raise DomainValidationError(
                "Otp must be a valid UUID"
            )
        if len(str(self.to_raw())) < 6 or len(str(self.to_raw())) > 6:
            raise DomainValidationError(
                "Otp must be 6 digits"
            )

        
        