def solution(players, callings):
    players_dict = {p:i for i,p in enumerate(players)}
    idx_dict = {i:p for i,p in enumerate(players)}
    
    for call in callings:
        current_idx = players_dict[call]
        front_idx = current_idx-1
        
        current_player = call
        front_player = idx_dict[front_idx]
        
        players_dict[front_player], players_dict[current_player] = current_idx, front_idx
        idx_dict[front_idx], idx_dict[current_idx] = current_player, front_player
        
    return list(idx_dict.values())