from pydantic import BaseModel


class DataRequest(BaseModel):
    sub_type: int
    listing_type: int
    tom: float
    building_age: int
    total_floor_count: int
    floor_no: int
    room_count: int
    size: float
    heating_type: int
    price_currency: int
    city: int
    district: int
    neighborhood: int

