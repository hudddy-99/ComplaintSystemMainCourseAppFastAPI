from datetime import datetime
from schemas.base import BaseComplaint
from models.enums import State


class ComplaintOut(BaseComplaint):
    created_at: datetime
    status: State