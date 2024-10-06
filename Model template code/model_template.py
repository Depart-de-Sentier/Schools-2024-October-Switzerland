from datetime import date
from pydantic import BaseModel
from typing import Optional
import pandas as pd


class IRI:
    # Can look up info
    pass


class Demand(BaseModel):
    product_iri: IRI
    properties: Optional[list]
    amount: float
    spatial_context: IRI = IRI("https://sws.geonames.org/6295630/")
    temporal_range: list[date, date]  # TBD


class RunConfig(BaseModel):
    outliers_raise_error: bool = False
    num_samples: int = 1000


class SentierModel:
    def __init__(self, demand: Demand, run_config: RunConfig):
        pass

    def get_model_data(self) -> list[pd.DataFrame]:  # Duck typing also fine
        pass

    def prepare(self) -> None:
        self.get_model_data()
        self.data_validity_checks()
        self.resample()

    def run(self) -> list[Demand]:
        pass
