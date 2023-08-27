from collections import defaultdict

def solution(word, pages):
    
    mydict = ['<a href=\"' , '<meta property=\"og:url\" content=\"']
    num = [len(mydict[0]),len(mydict[1])]
    
    url = []
    default = {}
    link = {}
    link_score = defaultdict(int)
    total = []
    
    w = len(word)
    word = word.lower()
    n = min(w, num[0], num[1])
    
    for page in pages:
        page = page.lower()
        i = 0
        memo = 0
        
        while i < len(page) - n + 1:
            if page[i:i+num[1]] == mydict[1]:
                temp = ''
                t = i+num[1]
                while True:
                    if page[t] == '\"':
                        break
                    temp += page[t]
                    t += 1
                url.append(temp)
                #default[temp] = 0
                link[temp] = list()
                i = t
                
            elif page[i:i+num[0]] == mydict[0]:
                temp = ''
                t = i+num[0]
                while True:
                    if page[t] == '\"':
                        break
                    temp += page[t]
                    t += 1
                link[url[-1]].append(temp)
                i = t
            elif page[i:i+w] == word:
                if not page[i-1].isalpha() and not page[i+w].isalpha():
                    memo += 1
                i += w
            i += 1
        default[url[-1]] = memo
    
    for key,value in link.items():
        n = len(value)
        k = default[key]
        for v in value:
            link_score[v] += k / n
        
    for i,u in enumerate(url):
        total.append((default[u] + link_score[u],i))
    
    answer = max(total, key = lambda x : (x[0],-x[1]))

    return answer[1]