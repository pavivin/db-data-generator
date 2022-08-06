from utils import base_types
from utils.type_generator import TypeGenerator as TG

GENERATE_TYPE = {
    "str": TG.generate_fake_str_data,
    "datetime": TG.generate_fake_timestamp_data,
    "date": TG.generate_fake_date_data,
    "float": TG.generate_fake_decimal_data,
    "int": TG.generate_fake_int_data,
}

CLASSES_TO_METHODS = {
    base_types.BaseStrType: TG.generate_fake_str_data,
    base_types.BaseTimestampType: TG.generate_fake_timestamp_data,
    base_types.BaseDateType: TG.generate_fake_date_data,
    base_types.BaseDecimalType: TG.generate_fake_decimal_data,
    base_types.BaseIntType: TG.generate_fake_int_data,
}
