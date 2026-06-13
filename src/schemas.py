from pydantic import BaseModel, Field

class IrisPredictionRequest(BaseModel):
    sepal_length: float = Field(..., description="Sepal length in cm", ge=0.0)
    sepal_width: float = Field(..., description="Sepal width in cm", ge=0.0)
    petal_length: float = Field(..., description="Petal length in cm", ge=0.0)
    petal_width: float = Field(..., description="Petal width in cm", ge=0.0)

class IrisPredictionResponse(BaseModel):
    prediction: str
    probabilities: list[float]
