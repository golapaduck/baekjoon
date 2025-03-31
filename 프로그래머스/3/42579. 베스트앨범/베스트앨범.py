def solution(genres, plays):
    
    answer = []
    genre_dict = {}
    temp = []
    
    for i in range(len(genres)):
        temp.append([genres[i],plays[i],i])
        
        try:
            genre_dict[genres[i]] += plays[i]
        except:
            genre_dict[genres[i]] = plays[i]
    
    temp = sorted(temp, key = lambda x: (x[0],-x[1],x[2]))
    genre_dict = sorted(genre_dict.items(),key = lambda x: -x[1])
    
    
    for genre in genre_dict:
            
        count = 0
        for item in temp:
            if item[0] == genre[0]:
                answer.append(item[2])
                count += 1
                if count >= 2:
                    break
                
    return answer