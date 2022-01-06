    
    # TODO 1: use a while loop to read the leader name from the line (format is "leader_name,leader_score")
    while (line[index] != ","):
      leader_name = leader_name + line[index] 
      index = index + 1