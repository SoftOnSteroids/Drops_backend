from fastapi import APIRouter
from datetime import date
from v1.db.models.dose import Dose
from v1.db.logic.doses import search_doses ,search_doses_by_date_range

router = APIRouter(prefix="/calendar",
                   tags=["calendar"],
                   responses={404: {"message": "No encontrado."}})

@router.get("/", response_model= list | None)
async def f_get_calendar(dict_path: dict) -> list[Dose] | None:
    return search_doses(dict_path)

@router.get("/range")
async def f_get_calendar_range(date_min: date, date_max: date | None = None) -> list[Dose] | None:
    
    return search_doses_by_date_range(date_min, date_max)
