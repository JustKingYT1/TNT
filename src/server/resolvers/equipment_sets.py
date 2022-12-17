from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import Equipments, EquipmentNameSets, EquipmentSets
from typing import Any


def new_name_set(set_name: EquipmentNameSets) -> None | dict:
    res = base_worker.execute(query="""INSERT INTO names_sets_of_equipment(name_of_equipment_set) 
                                       VALUES (?)
                                       RETURNING id""",
                              args=(set_name.name,))

    if type(res) != dict:
        return res[0]

    return res


def new_equipment(equipment: Equipments) -> None | dict:
    equip_id = base_worker.execute(query="INSERT INTO equipment(equipment, set_equipment_id)"
                                         "VALUES (?, ?)"
                                         "RETURNING id, set_equipment_id",
                                   args=(equipment.equipment, equipment.equip_set_id))
    res = base_worker.execute(query='INSERT INTO equipment_sets(name_equipment_set_id, equipment_id) VALUES (?, ?)',
                              args=(equip_id[1], equip_id[0]))

    return res


def get_equipment(equipment_id: int) -> Equipments | dict:
    res = base_worker.execute(
        query="SELECT id, equipment, set_equipment_id FROM equipment WHERE id=?",
        args=(equipment_id,),
        many=False)
    return None if not res else Equipments(
        id=res[0],
        equipment=res[1],
        equip_set_id=res[2])


def get_all_equipments() -> list[Equipments] | dict:
    equipment_list = base_worker.execute(
        query="SELECT id, equipment, set_equipment_id FROM equipment", many=True)

    res = []

    if equipment_list:
        for equipment in equipment_list:
            res.append(Equipments(
                id=equipment[0],
                equipment=equipment[1],
                equip_set_id=equipment[2]))

    return res


def upd_equipment(equipment_id: int, new_data: Equipments) -> None | dict:
    equip = base_worker.execute(query='UPDATE equipment '
                                      'SET (equipment, set_equipment_id) = (?, ?) '
                                      'WHERE id=(?)'
                                      'RETURNING set_equipment_id',
                                args=(new_data.equipment, new_data.equip_set_id, equipment_id))
    return base_worker.execute(query='UPDATE equipment_sets SET name_equipment_set_id=? WHERE equipment_id=?',
                               args=(equip[0], equipment_id))


def del_equipment(equipment_id: int) -> tuple[Any, Any] | dict:
    return base_worker.execute(query="DELETE FROM equipment_sets WHERE equipment_id=?",
                               args=(equipment_id,)), \
           base_worker.execute(query="DELETE FROM equipment WHERE id=(?)",
                               args=(equipment_id, equipment_id))


def get_equipment_name(equipment_name_id: int) -> EquipmentNameSets | dict:
    res = base_worker.execute(
        query="SELECT id, name_of_equipment_set FROM names_sets_of_equipment WHERE id=?",
        args=(equipment_name_id,))
    return None if not res else EquipmentNameSets(
        id=res[0],
        name=res[1])


def get_all_equipment_names() -> list[EquipmentNameSets] | dict:
    equipment_names_list = base_worker.execute(
        query="SELECT id, name_of_equipment_set FROM names_sets_of_equipment", many=True)

    res = []

    if equipment_names_list:
        for equipment_name in equipment_names_list:
            res.append(EquipmentNameSets(
                id=equipment_name[0],
                name=equipment_name[1]))

    return res


def upd_equipment_name(equipment_name_id: int, new_data: EquipmentNameSets) -> None | dict:
    return base_worker.execute(query='UPDATE names_sets_of_equipment '
                                     'SET (name_of_equipment_set) = (?) '
                                     'WHERE id=(?)',
                               args=(new_data.name, equipment_name_id))


def del_equipment_name(equipment_name_id: int) -> tuple[Any, Any, Any] | dict:
    res_1 = base_worker.execute(query="DELETE FROM names_sets_of_equipment WHERE id=(?)" ,args=(equipment_name_id,))
    res_2 = base_worker.execute(query="DELETE FROM equipment_sets WHERE name_equipment_set_id=?;", args=(equipment_name_id,))
    res_3 = base_worker.execute(query="DELETE FROM equipment WHERE set_equipment_id=?", args=(equipment_name_id,))
    return res_1, res_2, res_3


def get_equipment_set(equipment_set_id: int) -> EquipmentSets | dict:
    res = base_worker.execute(
        query="SELECT equipment_id, name_equipment_set_id FROM equipment_sets WHERE name_equipment_set_id=?",
        args=(equipment_set_id,))
    return None if not res else EquipmentSets(
        equip_id=res[0],
        name_set_id=res[1])


def get_all_equipment_sets() -> list[EquipmentSets] | dict:
    equipment_sets_list = base_worker.execute(
        query="SELECT name_equipment_set_id, equipment_id FROM equipment_sets", many=True)

    res = []

    if equipment_sets_list:
        for equipment_set in equipment_sets_list:
            res.append(EquipmentSets(
                equip_id=equipment_set[0],
                name_set_id=equipment_set[1]))

    return res
