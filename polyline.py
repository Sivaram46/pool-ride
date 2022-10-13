import requests


class Polyline:
    def __init__(self) -> None:
        self.polylines = []
        self.matches = []

    def add(self, ID: int, source: list, destination: list) -> None:
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


    @staticmethod
    def LCSubStr(string1: str, string2: str) -> str:

        m = len(string1)
        n = len(string2)

        result = 0
        end = 0

        length = [[0 for j in range(m+1)] for i in range(2)]

        currRow = 0
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if (i == 0 or j == 0):
                    length[currRow][j] = 0

                elif (string1[i - 1] == string2[j - 1]):
                    length[currRow][j] = length[1 - currRow][j - 1] + 1

                    if (length[currRow][j] > result):
                        result = length[currRow][j]
                        end = i - 1
                else:
                    length[currRow][j] = 0

            currRow = 1 - currRow

        if (result == 0):
            return "-1"

        return string1[end - result + 1: end + 1]

    def _is_matching(self, polyline1: str, polyline2: str) -> bool:

        if len(polyline1) < len(polyline2):
            polyline1, polyline2 = polyline2, polyline1

        lcs = self.LCSubStr(polyline1, polyline2)
        com_head_len = 2
        n_lcs = len(lcs) 
        n_line1 = len(polyline1) - com_head_len
        n_line2 = len(polyline2) - com_head_len

        # Assuming common header is 1st 2 chars
        if lcs == polyline1[:com_head_len] or lcs == "-1":
            return False
        # Fully contained
        elif (lcs == polyline1[com_head_len: ] or lcs == polyline2[com_head_len: ]):
            return True
        # LCS more than 50% of both:
        elif (n_lcs > n_line1/2 and n_lcs > n_line2/2):
            return True
        else:
            return False

    def __match_polylines(self):
        if len(self.polylines) < 2:
            return
        id1, polyline1 = self.polylines[-1]
        for idx, (id2, polyline2) in enumerate(self.polylines[:-1]):
            if self._is_matching(polyline1, polyline2):
                # share of polyline1
                share = self._get_fare_share(polyline1, polyline2)
                del self.polylines[-1]
                del self.polylines[idx]
                self.matches.append([id1, id2, share])

    def _get_fare_share(self, polyline1: str, polyline2: str) -> float:
        is_poly_swapped = False
        if len(polyline1) < len(polyline2):
            is_poly_swapped = True
            polyline1, polyline2 = polyline2, polyline1

        # lcs = self.LCSubStr(polyline1, polyline2)
        com_head_len = 2
        # n_lcs = len(lcs) 
        n_line1 = len(polyline1) - com_head_len
        n_line2 = len(polyline2) - com_head_len

        fare_share = min(1, n_line1/(n_line1+n_line2))
        if is_poly_swapped:
            fare_share = 1 - fare_share
        return fare_share

    @staticmethod
    def __get_polyline(source: list, destination: list) -> str:
        api = f'https://router.hereapi.com/v8/routes?transportMode=car&origin={source[0]},{source[0]}&destination={destination[0]},{destination[0]}&return=polyline,summary&apikey=4zrYS3HwHMWmrB6jcbGjNRltDgVws9KsQXl_BD4wHgs'
        polyline = requests.get(api)
        return polyline.json()['routes'][0]['sections'][0]['polyline']

if __name__ == '__main__':
    polyline = Polyline()
    polyline.add(123, [52.5308,13.3847], [52.5264,13.3686])
    polyline.add(122, [52.5308,13.3847], [52.5264,13.3686])
    print(polyline.check_status(122))
