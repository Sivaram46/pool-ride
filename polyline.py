import requests

POLYLINES = []
MATCHES = []

def get_polyline(source: list[float], destination: list[float]) -> str:
    api = f'https://router.hereapi.com/v8/routes?transportMode=car&origin={source[0]},{source[0]}&destination={destination[0]},{destination[0]}&return=polyline,summary&apikey=GpDd-xA4yTAP0JdcIoNv0_BtCj_CbzFhUI75hRNdiRk'
    polyline = requests.get(api)
    return polyline.json()['routes'][0]['sections'][0]['polyline']

def submit_action(ID: int, source: list[float], destination: list[float]) -> None:
    polyline = get_polyline(source, destination)
    POLYLINES.append([ID, polyline])

def is_matching(polyline1: str, polyline2: str) -> bool:
    return polyline1 == polyline2

def match_polylines():
    for idx1, val1 in enumerate(POLYLINES[:]):
        for idx2, val2 in enumerate(POLYLINES[:][idx1+1:]):
            if is_matching(val1[1], val2[1]):
                del POLYLINES[idx1]
                del POLYLINES[idx2]
                MATCHES.append([val1[0], val2[0]])

submit_action(123, [52.5308,13.3847], [52.5264,13.3686])
submit_action(122, [52.5308,13.3847], [52.5264,13.3686])
match_polylines()
print(POLYLINES)
print(MATCHES)