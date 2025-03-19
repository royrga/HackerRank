def minion_game(string):
    # your code goes here
    k_points = 0
    s_points = 0
    k_words = []
    s_words = []
    for i in range(len(string)):
        if string[i].lower() in {'a','e','i','o','u'}:
            for j in range(i+1,len(string)+1):
                points = 0
                points += 1
                # points += string.count(string[i:j])-1 if string.find(string[i:j]) != -1 else 0
                k_points += points
                k_words.append([string[i:j],points])
        else:
            for j in range(i+1,len(string)+1):
                points = 0
                points += 1
                # points += string.count(string[i:j])-1 if string.count(string[i:j]) > 0 else 0
                s_points += points
                s_words.append([string[i:j],points])

    # print(k_words)
    # print(s_words)
    if k_points > s_points:
        print(f"Kevin {k_points}")
    elif k_points == s_points:
        print("Draw")
    else:
        print(f"Stuart {s_points}")
    



minion_game("BANANA")
# minion_game("BANANANAAAS")
