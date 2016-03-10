from collections import deque
class ListeningSongs:
    def listen(self, durations1, durations2, minutes, T): 
        if type(durations1) == int:
            durations1 = deque([durations1])
        else:
            durations1 = deque(sorted(list(durations1)))
        if type(durations2) == int:
            durations2 = deque([durations2])
        else:
            durations2 = deque(sorted(list(durations2)))
        seconds = minutes * 60
        listened = 0
        while listened < T * 2:
            if (not durations1) or (not durations2):
                return(-1)
            songs = [durations1.popleft(), durations2.popleft()]
            for s in songs:
                listened += 1
                seconds -= s
                if seconds < 0:
                    return(-1)
        durations = deque(sorted(list(durations1) + list(durations2)))
        while durations:
            song = durations.popleft()
            seconds -= song
            listened += 1
            if seconds < 0:
                return(listened - 1)
        return(listened)