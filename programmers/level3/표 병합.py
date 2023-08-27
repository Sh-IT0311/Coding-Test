from collections import defaultdict

def solution(commands):
    answer = []
    
    data = [[''] * 51 for _ in range(51)]
    values = defaultdict(set)
    index2merge = [[0] * 51 for _ in range(51)]
    merge2index = [[] for _ in range(2551)]
    merge = 50
    for i in range(1,51):
        for j in range(1,51):
            merge += 1
            index2merge[i][j] = merge
            merge2index[merge].append((i,j))

    for command in commands:
        oper, *temp = command.split()
        
        if oper == 'UPDATE':
            if len(temp) == 3:
                (r, c), value = map(int, temp[:2]), temp[2]
                
                if data[r][c] != '':
                    other = data[r][c]
                    for x, y in merge2index[index2merge[r][c]]:
                        values[other].remove((x,y))
                        values[value].add((x,y))
                        data[x][y] = value
                        
                else:
                    for x, y in merge2index[index2merge[r][c]]:
                        values[value].add((x,y))
                        data[x][y] = value
                
            elif len(temp) == 2:
                value1, value2 = temp
                values[value1] = values[value1]
                for x, y in values.pop(value1):
                    data[x][y] = value2
                    values[value2].add((x,y))
        
        elif oper == 'MERGE':
            r1, c1, r2, c2 = map(int, temp)

            if r1 == r2 and c1 == c2:
                continue

            merge1 = index2merge[r1][c1]
            merge2 = index2merge[r2][c2]
            
            if merge1 == merge2:
                continue
            
            indices1 = merge2index[merge1]
            indices2 = merge2index[merge2]
            
            if data[r1][c1] != '': # integrate to 1
                value = data[r1][c1]
                if data[r2][c2] != '':
                    other = data[r2][c2]
                    for x, y in indices2:
                        values[other].remove((x,y))
                        values[value].add((x,y))
                        data[x][y] = value
                        indices1.append((x,y))
                        index2merge[x][y] = merge1
                else:
                    for x, y in indices2:
                        values[value].add((x,y))
                        data[x][y] = value
                        indices1.append((x,y))
                        index2merge[x][y] = merge1
            else:
                if data[r2][c2] != '': # integrate to 2
                    value = data[r2][c2]
                    for x, y in indices1:
                        values[value].add((x,y))
                        data[x][y] = value
                        indices2.append((x, y))
                        index2merge[x][y] = merge2
                else:
                    for x, y in indices2:
                        indices1.append((x,y))
                        index2merge[x][y] = merge1

        elif oper == 'UNMERGE':
            r, c = map(int, temp)
            
            value = data[r][c]
            merge = index2merge[r][c]
            indices = merge2index[merge]
            
            if value != '':
                for x, y in indices:
                    data[x][y] = ''
                    values[value].remove((x,y))
                    index2merge[x][y] = 50 * x + y
                    merge2index[index2merge[x][y]] = [(x, y)]    
                data[r][c] = value
                values[value].add((r,c))
                
            else:
                for x, y in indices:
                    index2merge[x][y] = 50 * x + y
                    merge2index[index2merge[x][y]] = [(x, y)]
            
        elif oper == 'PRINT':
            r, c = map(int, temp)
            if data[r][c] == '':
                answer.append('EMPTY')
            else:
                answer.append(data[r][c])
    
    return answer