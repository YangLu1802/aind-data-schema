"""Classes to define reagents"""

from datetime import date

from pydantic import Field

from aind_data_schema.base import AindModel, PIDName

class Reagent(AindModel):
    """Description of reagent used in procedure"""

    name: str = Field(..., title="Name")
    source: str = Field(..., title="Source")
    rrid: Optional[PIDName] = Field(None, title="Research Resource ID")
    lot_number: str = Field(..., title="Lot number")
    expiration_date: Optional[date] = Field(None, title="Lot expiration date")
