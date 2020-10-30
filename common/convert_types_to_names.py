from models import SensorValueTypeModel


def convert_types_to_names(area):
    result = {}

    a = area.as_dict()
    for v_type in a:
        value = a.get(v_type)
        v_name = getattr(SensorValueTypeModel.query.filter(
            SensorValueTypeModel.type == v_type).first(), 'name', None)

        if v_name:
            result[v_name] = value
        else:
            result[v_type] = value

    return result
