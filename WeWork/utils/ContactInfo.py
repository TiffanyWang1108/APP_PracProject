"""
Name : ContactInfo.py
Author  : Tiffany
Time : 2022/8/30 17:31
DESC: 
"""
from faker import Faker

from WeWork.utils.log_utils import logger


class ContactInfo:
    @classmethod
    def get_name(cls):
        name = Faker('zh_CN').name()
        logger.info(f"name:{name}")
        return name

    @classmethod
    def get_phone(cls):
        phone = Faker('zh_CN').phone_number()
        logger.info(f"phone:{phone}")
        return phone


if __name__ == '__main__':
    ContactInfo.get_name()
    ContactInfo.get_phone()
