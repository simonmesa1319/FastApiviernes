from pydantic import BaseModel, Field
from datetime import date

class UsuarioDTOPeticion(BaseModel):
    nombre:str
    edad:int
    telefono:str
    correo:str 
    contraseña:str
    fechaRegistro:date
    ciudad:str 
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id:int
    nombre:str
    telefono: str
    ciudad: str
    class Config:
        orm_mode=True

'''class GastoDTOPeticion(BaseModel):
    id:int
    monto:float
    fecha:date
    descripcion:str
    nombre:str
    class Config:
        orm_mode=True

class GastoDTORespuesta(BaseModel):
    monto:float
    fecha:date
    descripcion:str
    class Config:
        orm_mode=True'''

