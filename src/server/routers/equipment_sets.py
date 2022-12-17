import fastapi
from server.sql_base.models import Equipments, EquipmentSets, EquipmentNameSets
from server.resolvers.equipment_sets import get_equipment_name, get_equipment, del_equipment_name, upd_equipment_name, new_equipment, get_all_equipments, get_all_equipment_names, upd_equipment, get_all_equipment_sets, del_equipment, get_equipment_set, new_name_set


equipment_router = fastapi.APIRouter(prefix='/equipments', tags=['Equipments'])

equipment_names_router = fastapi.APIRouter(prefix='/equipment/names', tags=['EquipmentNames'])

equipment_sets_router = fastapi.APIRouter(prefix='/equipment/sets', tags=['EquipmentSets'])


@equipment_router.get("/")
def start_page_1():
    return f"Hello new user!"


@equipment_names_router.get("/")
def start_page_2():
    return f"Hello new user!"


@equipment_sets_router.get("/")
def start_page_3():
    return f"Hello new user!"


@equipment_router.get("/get/{equipment_id}/", response_model=Equipments | dict)
def get_equipment_rout(equipment_id: int) -> Equipments | dict:
    return get_equipment(equipment_id)


@equipment_router.get("/get/", response_model=list[Equipments] | dict)
def get_equipments_all() -> list[Equipments] | dict:
    return get_all_equipments()


@equipment_router.post("/create/", response_model=int | dict)
def create_equipment(equipment: Equipments) -> int | dict:
    return new_equipment(equipment)


@equipment_router.put("/update/{equipment_id}/", response_model=None | dict)
def update_equipment(equipment_id: int, new_data: Equipments) -> None | dict:
    return upd_equipment(equipment_id, new_data)


@equipment_router.delete("/delete/{equipment_id}/", response_model=None | dict)
def delete_equipment(equipment_id) -> None | dict:
    return del_equipment(equipment_id)


@equipment_names_router.get("/get/{equipment_name_id}/", response_model=EquipmentNameSets | dict)
def get_names_equipment_rout(equipment_name_id: int) -> EquipmentNameSets | dict:
    return get_equipment_name(equipment_name_id)


@equipment_names_router.get("/get/", response_model=EquipmentNameSets | dict)
def get_all_equipment_names_rout() -> list[EquipmentNameSets] | dict:
    return get_all_equipment_names()


@equipment_names_router.post("/create/", response_model=int | dict)
def create_equipment_name(equipment_name: EquipmentNameSets) -> int | dict:
    return new_name_set(equipment_name)


@equipment_names_router.put("/update/{equipment_name_id}/", response_model=None | dict)
def update_equipment_name(equipment_name_id: int, new_data: EquipmentNameSets) -> None | dict:
    return upd_equipment_name(equipment_name_id, new_data)


@equipment_names_router.delete("/delete/{equipment_name_id}/", response_model=None | dict)
def delete_equipment_name(equipment_name_id) -> None | dict:
    return del_equipment_name(equipment_name_id)


@equipment_sets_router.get("/get/{equipment_set_id}/", response_model=EquipmentSets | dict)
def get_equipment_set_rout(equipment_set_id: int) -> EquipmentSets | dict:
    return get_equipment_set(equipment_set_id)


@equipment_sets_router.get("/get/")
def get_equipment_sets_all() -> list[EquipmentSets] | dict:
    return get_all_equipment_sets()

