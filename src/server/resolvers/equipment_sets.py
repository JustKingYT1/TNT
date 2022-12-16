from server.sql_base.db_tv_channels import base_worker
from server.sql_base.models import Equipments, EquipmentNameSets, EquipmentSets


def new_name_set(set_name: EquipmentNameSets) -> int | dict:
    res = base_worker.execute(query="""INSERT INTO names_sets_of_equipment(name_of_equipment_set) 
                                       VALUES (?)
                                       RETURNING id""",
                              args=(set_name.name,))
    if type(res) != dict:
        return res[0]

    return res


def new_equipment(equipment: Equipments) -> int | dict:
    res = base_worker.execute(query="INSERT INTO equipment(equipment)"
                                    "VALUES (?)"
                                    "RETURNING id",
                              args=(equipment.equipment,))
    if type(res) != dict:
        return res[0]

    return res


def new_set_of_equipment(set_equipment: EquipmentSets) -> int | dict:
    res = base_worker.execute(query="INSERT INTO equipment_sets(name_equipment_set_id, equipment_id) "
                                    "VALUES (?, ?)"
                                    "RETURNING id",
                              args=(set_equipment.equip_id, set_equipment.name_set_id))

    if type(res) != dict:
        return res[0]

    return res


def get_equipment(equipment_id: int) -> Equipments:
    res = base_worker.execute(
        query="SELECT id, equipment FROM equipment WHERE id=?",
        args=(equipment_id,),
        many=False)
    return None if not res else Equipments(
        id=res[0],
        equipment=res[1])


def get_all_equipments() -> list[Equipments] | dict:
    equipment_list = base_worker.execute(
        query="SELECT id, equipment FROM equipment", many=True)

    res = []

    if equipment_list:
        for equipment in equipment_list:
            res.append(Equipments(
                id=equipment[0],
                equipment=equipment[1]))

    return res


def upd_equipment(equipment_id: int, new_data: Equipments) -> None:
    return base_worker.execute(query='UPDATE equipment '
                                     'SET (equipment) = (?) '
                                     'WHERE id=(?)',
                               args=(new_data.equipment, equipment_id))


def del_equipment(equipment_id: int) -> None:
    return base_worker.execute(query="DELETE FROM equipment WHERE id=(?)",
                               args=(equipment_id,))


def get_equipment_name(equipment_name_id: int) -> EquipmentNameSets:
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


def upd_equipment_name(equipment_name_id: int, new_data: EquipmentNameSets) -> None:
    return base_worker.execute(query='UPDATE names_sets_of_equipment '
                                     'SET (name_of_equipment_set) = (?) '
                                     'WHERE id=(?)',
                               args=(new_data.name, equipment_name_id))


def del_equipment_name(equipment_name_id: int) -> None:
    return base_worker.execute(query="DELETE FROM names_sets_of_equipment WHERE id=(?)",
                               args=(equipment_name_id,))


def get_equipment_set(equipment_set_id: int) -> EquipmentSets:
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


def del_equipment_set(equipment_set_id: int) -> None:
    return base_worker.execute(query="DELETE FROM equipment_sets WHERE name_equipment_set_id=(?)",
                               args=(equipment_set_id,))
