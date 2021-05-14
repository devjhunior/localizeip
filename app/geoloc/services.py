from ..configs import API_TOKEN
import ipinfo


class Service:

    def get_geoloc(self, ip):
        try:
            handler = ipinfo.getHandler(API_TOKEN)
            details = handler.getDetails(ip)
        except ipinfo.exceptions as _err:
            print(f'Erro ao pegar informações IP: {_err}')
            raise _err
        return details.all
