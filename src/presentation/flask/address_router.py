from flask import request, Blueprint

from src.application.address_service import AddressService

address = Blueprint('address', __name__, url_prefix='/address')


@address.route('/sido')
def get_sido():
    address_service = AddressService()
    sido_list = address_service.get_sido()
    return sido_list


@address.route('/sigungu')
def get_sigungu():
    sido = request.args.get('sido')
    address_service = AddressService()
    sigungu_list = address_service.get_sigungu(sido)
    return sigungu_list


@address.route('/bjdong')
def get_bjdong():
    sido = request.args.get('sido')
    sigungu = request.args.get('sigungu')
    address_service = AddressService()
    bjdong_list = address_service.get_bjdong(sido, sigungu)
    return bjdong_list


@address.route('/code')
def get_address_code():
    sido = request.args.get('sido')
    sigungu = request.args.get('sigungu')
    bjdong = request.args.get('bjdong')
    address_service = AddressService()
    code = address_service.get_code(sido, sigungu, bjdong)
    return str(code)
