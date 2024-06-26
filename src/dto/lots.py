import datetime
from typing import Any
from uuid import UUID

from fastapi import Form
from pydantic import BaseModel


class LotDTORead(BaseModel):
    id: UUID
    title: str | None
    start_bet: int | None
    winner_uid: Any | None
    current_bet: int | None
    is_active: bool | None
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    closed_at: datetime.datetime | None

    class Config:
        from_attributes = True


class LotDTOAdd(BaseModel):
    title: str
    start_bet: int
    description: str

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        start_bet: int = Form(...),
    ):
        return cls(title=title, description=description, start_bet=start_bet)


class LotDTOEdit(BaseModel):
    id: UUID
    # title: str | None
    current_bet: int | None

    @classmethod
    def as_form(
        cls,
        id: UUID = Form(...),
        # title: str = Form(...),
        current_bet: int = Form(...),
    ):
        return cls(
            id=id,
            # title=title,
            current_bet=current_bet,
        )


class LotDTOGet(BaseModel):
    id: UUID

    @classmethod
    def as_form(
        cls,
        id: UUID = Form(...),
    ):
        return cls(id=id)


class LotDTOArchive(BaseModel):
    id: UUID
    is_active: bool = False

    @classmethod
    def as_form(
        cls,
        id: UUID = Form(...),
        is_active: bool = Form(False),
    ):
        if is_active is True:  # Если передано значение True, заменяем его на False
            is_active = False
        return cls(id=id, is_active=is_active)


class LotDTOWinner(BaseModel):
    lot_id: UUID

    @classmethod
    def as_form(
        cls,
        lot_id: UUID = Form(...),
    ):
        return cls(lot_id=lot_id)


class LotDTOGets(BaseModel):
    id: UUID
    title: str | None
    start_bet: int | None
    winner_uid: str | None
    current_bet: int | None
    is_active: bool | None
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    closed_at: datetime.datetime | None

    @classmethod
    def as_form(
        cls,
        id: UUID = Form(...),
        title: str | None = Form(None),
        start_bet: int | None = Form(None),
    ):
        return cls(id=id, title=title, start_bet=start_bet)


class LotDTODelete(BaseModel):
    id: UUID

    @classmethod
    def as_form(
        cls,
        id: UUID = Form(...),
    ):
        return cls(id=id)


class LotDTOWinner(BaseModel):
    id: UUID
    winner_uid: UUID
    closed_bet: float

    @classmethod
    def as_form(
        cls,
        id: UUID = Form(...),
        winner_uid: UUID = Form(...),
        closed_bet: float = Form(...),
    ):
        return cls(
            id=id,
            winner_uid=winner_uid,
            closed_bet=closed_bet,
        )


class LotDTOCurrentBet(BaseModel):
    lot_id: UUID
    user_id: UUID
    current_bet: float

    @classmethod
    def as_form(
        cls,
        lot_id: UUID = Form(...),
        user_id: UUID = Form(...),
        current_bet: float = Form(...),
    ):
        return cls(
            lot_id=lot_id,
            user_id=user_id,
            current_bet=current_bet,
        )
