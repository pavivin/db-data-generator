def validate_dataclass(data_class):
    for field_name, field in data_class.__dataclass_fields__.items():
        field_attr = getattr(data_class, field_name)
        if isinstance(type(field_attr), type):
            ...
        else:
            if not isinstance(field_attr, field.type):
                raise ValueError
