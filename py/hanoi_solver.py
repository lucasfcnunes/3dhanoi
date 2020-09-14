# dê um replace em "_to" -> "to"; "_from" -> "from"; "_using" -> "using"

TOTAL_DISK_COUNT = 4 #n
START_TOWER, WORK_TOWER, END_TOWER = 1, 2, 3 # enum {START_TOWER, WORK_TOWER, END_TOWER}
towers = {
    START_TOWER: list(range(TOTAL_DISK_COUNT,0,-1)), #[TOTAL_DISK_COUNT, ..., 3, 2, 1]
    WORK_TOWER:[],
    END_TOWER:[]
    }

class Movement:
    '''
class Movement:
	var from : int
	var to : int
    '''
    def __init__(self, _from: int, _to: int):
        self._from = _from
        self._to = _to

    def __repr__(self): #ignore isso aqui (só server para pretty print da class instance)
        return "%s(%r)" % (self.__class__, self.__dict__)

moves = []

def solve(
    disks=TOTAL_DISK_COUNT,
    _from=towers[START_TOWER],
    _to=towers[END_TOWER],
    _using=towers[WORK_TOWER]
    ):
    if disks:
        solve(disks=disks-1, _from=_from, _to=_using, _using=_to)

        move = Movement(0,0)
        for tower in towers:
            if _from is towers[tower]:
                move._from = tower
            elif _to is towers[tower]:
                move._to = tower

        moves.append(move) # movement_queue.push_back(objeto)
        _to.append(_from.pop())
        print(towers)

        solve(disks=disks-1, _from=_using, _to=_to, _using=_from)

print("PROBLEM:", towers)
print("SOLUTION:")
solve()

print(moves)
