from pydantic import BaseModel, validator  # pylint: disable=no-name-in-module


class AddressBase(BaseModel):
    crypto: str


class AddressRequest(AddressBase):
    @validator("crypto")
    def three_char_long(cls, value):  # pylint: disable=no-self-argument
        if len(value) != 3:
            raise ValueError("has to be 3 char long")
        return value


class AddressResponse(AddressBase):
    id: int
    address: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {"id": 1, "crypto": "EXM", "address": "example_address"}}
