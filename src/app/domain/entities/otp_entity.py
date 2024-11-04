from dataclasses import dataclass

from app.domain.common.entity import DomainEntity
from app.domain.value_objects.otp_created_at_value_object import OtpCreatedAt
from app.domain.value_objects.otp_expires_at_value_object import OtpExpiresAt
from app.domain.value_objects.otp_value_object import Otp
from app.domain.value_objects.action_uuid_value_object import ActionUUID


@dataclass
class OtpEntity(DomainEntity[ActionUUID]):
    uuid: ActionUUID
    otp: Otp
    otp_created_at: OtpCreatedAt
    otp_expires_at: OtpExpiresAt