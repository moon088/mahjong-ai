#特徴量作成:七対子の向聴数

def calculate_titoitu_shanten(hand):
    if len(hand) != 13:
        return "error"

    count_of_kantu = 0
    for tile in hand:
        count = hand.count(tile)
        if count >= 4:
            count_of_kantu += 1
            
    allcount_of_kantu = int(count_of_kantu/4)        
    unique_tiles = set(hand)
    pairs_count = 0
    for tile in unique_tiles:
        count = hand.count(tile)
        pairs_count += count // 2

    shanten = 6 - pairs_count + allcount_of_kantu
    return shanten

#test
#hand = ['m1','m1','m4','m7','p1','p2','p5','p6','s1','s5','s7','s7','s9']
#result = calculate_titoitu_shanten(hand)
#print(result)