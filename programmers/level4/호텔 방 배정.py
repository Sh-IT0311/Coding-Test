import sys
sys.setrecursionlimit(300000)

def solution(k, room_number):
    rooms = dict()
    
    def find_rooms(room):
        if room not in rooms.keys():
            rooms[room] = room + 1
        
        else:
            rooms[room] = find_rooms(rooms[room])
        
        return rooms[room]
    
    for room in room_number:
        find_rooms(room)
    
    return list(rooms.keys())