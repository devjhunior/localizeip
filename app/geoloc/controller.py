from .services import Service


class Controller:
    service = Service()

    def get_geoloc(self, ip):
        return self.service.get_geoloc(ip)
