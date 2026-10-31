def process_performance_requests(requests):
    processed = {}
    big = 0
    
    requests.sort()
    
    for i in requests: 
        if i not in processed:
            processed[i[1]] = i[0] 
        


    processed.append(big)    

    