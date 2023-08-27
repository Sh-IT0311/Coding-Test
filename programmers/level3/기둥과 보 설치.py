def possible(answer):
    for x,y,what in answer:
        if what == 0:
            if (y == 0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer):
                continue
            return False
        else:
            if ([x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer)):
                continue
            return False
    return True

def solution(n, build_frame):

    answer = []

    for x,y,what,make in build_frame:
        if  make == 1:
            answer.append([x,y,what])
            if not possible(answer):
                answer.remove([x,y,what])
        else:
            if [x,y,what] in answer:
                answer.remove([x,y,what])
                if not possible(answer):
                    answer.append([x,y,what])

    answer.sort()
    return answer