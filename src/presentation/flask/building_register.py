from flask import request, Blueprint

from src.application.building_register_service import BuildingRegisterService
from src.infrastructure.register_columns_repository import RegisterTitleColumns

register = Blueprint('register', __name__)


@register.route('/building-register/title', methods=['POST'])
def get_general_register():
    sigungu_code = request.args.get('sigungu_code')
    bjdong_code = request.args.get('bjdong_code')
    data = request.json
    columns = [RegisterTitleColumns(eng=column['eng'], kor=column['kor']) for column in data.get('columns')]
    register_service = BuildingRegisterService()
    registers = register_service.get_title_registers(sigungu_code, bjdong_code, columns)
    return registers


@register.route('/building-register/columns')
def get_register_columns():
    register_service = BuildingRegisterService()
    columns = register_service.get_columns()
    return str(columns)
