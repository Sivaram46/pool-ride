import requests

class Polyline:
    def __init__(self) -> None:
        self.polylines = []
        self.matches = []

    def add(self, ID: int, source: list[float], destination: list[float]) -> None:
        polyline = Polyline.__get_polyline(source, destination)
        self.polylines.append([ID, polyline])

    def is_matching(self, polyline1: str, polyline2: str) -> bool:
        return polyline1 == polyline2

    def match_polylines(self):
        for idx1, val1 in enumerate(self.polylines[:]):
            for idx2, val2 in enumerate(self.polylines[:][idx1+1:]):
                if self.is_matching(val1[1], val2[1]):
                    del self.polylines[idx1]
                    del self.polylines[idx2]
                    self.matches.append([val1[0], val2[0]])

    @staticmethod
    def __get_polyline(source: list[float], destination: list[float]) -> str:
        api = f'https://router.hereapi.com/v8/routes?transportMode=car&origin={source[0]},{source[0]}&destination={destination[0]},{destination[0]}&return=polyline,summary&apikey=GpDd-xA4yTAP0JdcIoNv0_BtCj_CbzFhUI75hRNdiRk'
        polyline = requests.get(api)
        return polyline.json()['routes'][0]['sections'][0]['polyline']

if __name__ == '__main__'
    polyline = Polyline()
    polyline.add(123, [52.5308,13.3847], [52.5264,13.3686])
    polyline.add(122, [52.5308,13.3847], [52.5264,13.3686])
    polyline.match_polylines()
    print(polyline.polylines)
    print(polyline.matches)