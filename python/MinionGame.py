def minion_game(string):
    # your code goes here
    k_points = 0
    s_points = 0
    k_words = []
    s_words = []
    l_string = len(string)
    for i in range(l_string):
        if string[i] in 'AEIOU':
            k_points += len(string[i:])
        else:
            s_points += len(string[i:])

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
