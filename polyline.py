import requests

class Polyline:
    def __init__(self) -> None:
        self.polylines = []
        self.matches = []

    def add(self, ID: int, source: list[float], destination: list[float]) -> None:
        polyline = Polyline.__get_polyline(source, destination)
        self.polylines.append([ID, polyline])
        self.__match_polylines()

    def check_status(self, ID) -> int:
        try:
            idx = next(i for i, j in enumerate(self.matches) if j[0] == ID)
            match = self.matches[idx]
            del self.matches[idx]
        except:
            match = [-1, -1]
        return match

    def remove(self, ID: int):
        try:
            idx = next(i for i, j in enumerate(self.polylines) if j[0] == ID)
            del self.polylines[idx]
        except:
            print('No such ID')

    def __is_matching(self, polyline1: str, polyline2: str) -> bool:
        return polyline1 == polyline2

    def __match_polylines(self):
        if len(self.polylines) < 2: return
        id1, polyline1 = self.polylines[-1]
        for idx, (id2, polyline2) in enumerate(self.polylines[:-1]):
            if self.__is_matching(polyline1, polyline2):
                del self.polylines[-1]
                del self.polylines[idx]
                self.matches.append([id1, id2])

    @staticmethod
    def __get_polyline(source: list[float], destination: list[float]) -> str:
        api = f'https://router.hereapi.com/v8/routes?transportMode=car&origin={source[0]},{source[0]}&destination={destination[0]},{destination[0]}&return=polyline,summary&apikey=GpDd-xA4yTAP0JdcIoNv0_BtCj_CbzFhUI75hRNdiRk'
        polyline = requests.get(api)
        return polyline.json()['routes'][0]['sections'][0]['polyline']

if __name__ == '__main__':
    polyline = Polyline()
    polyline.add(123, [52.5308,13.3847], [52.5264,13.3686])
    polyline.add(122, [52.5308,13.3847], [52.5264,13.3686])
    # print(polyline.polylines)
    # print(polyline.matches)
    print(polyline.check_status(122))