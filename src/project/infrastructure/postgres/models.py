from sqlalchemy.orm import Mapped, mapped_column
from project.infrastructure.postgres.database import Base

class Meals(Base):
    __tablename__ = "meals"

    id_meal: Mapped[str] = mapped_column(primary_key=True)
    count_ingredients: Mapped[int]
    gruppa: Mapped[str]
    season: Mapped[str]
    weigth: Mapped[int]
    count_pors: Mapped[int]
    prepering_time: Mapped[int]