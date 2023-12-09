from typing import Any, Union, List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy import exc
from fastapi_pagination import Page, add_pagination, paginate
from .dependencies import UOWDep
from src.dto.lots import (
    LotDTOAdd,
    LotDTODelete,
    LotDTOEdit,
    LotDTOGets,
    LotDTOGet,
    LotDTORead,
)
from src.crud.lots import LotsService


router = APIRouter()


@router.put("/")
async def move_lot_to_archive(
    uow: UOWDep,
):
    pass


@router.post("/", response_model=Union[LotDTOAdd, Any])
async def create_lot(
    uow: UOWDep,
    lot: LotDTOAdd = Depends(LotDTOAdd.as_form),
):
    created_lot = await LotsService().add_lot(uow, lot)
    return created_lot


@router.post("/one", response_model=Union[LotDTORead, Any])
async def get_lot(uow: UOWDep, lot: LotDTOGet = Depends(LotDTOGet.as_form)):
    try:
        result = await LotsService().get_lot(uow, lot)
        return result
    except exc.NoResultFound:
        return JSONResponse(status_code=404, content={"error": "Lot Not Found"})


@router.get("/all", response_model=Page[Union[List[LotDTOGets], Any]])
async def get_lots(
    uow: UOWDep,
):
    lots = await LotsService().get_lots(uow)
    return paginate(lots)


@router.delete("/")
async def delete_lot(uow: UOWDep, lot: LotDTODelete = Depends(LotDTODelete.as_form)):
    lot_id = await LotsService().delete_lot(uow, lot)
    if lot_id is True:
        return {"is_deleted": True}
    return JSONResponse(status_code=404, content={"error": "Lot Not Found"})


@router.patch("/", response_model=Union[LotDTOEdit, Any])
async def edit_lot(uow: UOWDep, lot: LotDTOEdit = Depends(LotDTOEdit.as_form)):
    """Изменяет ставку лота когда её перебивает другой аукционер"""
    try:
        result = await LotsService().edit_lot(uow, lot)
        if result is True:
            return result
        return JSONResponse(
            status_code=422,
            content={"error": "Your value should be lower than current bet"},
        )

    except exc.NoResultFound:
        return JSONResponse(status_code=404, content={"error": "Lot Not Found"})
