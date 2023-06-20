from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from src.apis.address.models import Address
from src.apis.address.schemas import AddressRequest, AddressResponse
from src.lib.coins import Coin
from src.lib.core.dependancies import get_db
from src.lib.core.exceptions import CoinNotSupportedException

address_router = APIRouter(prefix="/address", tags=["address"])


@address_router.get("/", response_model=list[AddressResponse], summary="Get all addresses")
def get_all(session: Session = Depends(get_db)) -> list:
    return Address.get_all(session)


@address_router.get(
    "/{address_id}",
    response_model=AddressResponse,
    summary="Get address by ID",
    responses={status.HTTP_404_NOT_FOUND: {"model": str}},
)
def get_by_id(address_id: int = Path(ge=0), session: Session = Depends(get_db)) -> dict:
    if address := Address.get_by_id(address_id, session):
        return address
    raise HTTPException(status.HTTP_404_NOT_FOUND, "Address not found")


@address_router.post(
    "/generate",
    response_model=AddressResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Generate address",
    responses={status.HTTP_400_BAD_REQUEST: {"model": str}},
)
def generate(address_request: AddressRequest, session: Session = Depends(get_db)) -> dict:
    try:
        coin = Coin.from_string(address_request.crypto.lower())
        generated_address = coin.create_address()
    except CoinNotSupportedException as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Coin not supported") from e
    return Address.create(generated_address, address_request.crypto.lower(), session=session)
