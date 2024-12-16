class Element:
    def __init__(self,name,symbol,score_per_elem,min_number_in_board):
        self.name = name
        self.symbol = symbol
        self.score_per_elem = score_per_elem
        self.min_number_in_board= min_number_in_board

elements_data = {
                "Coin": ['$',1,10],
                "Empty" : ['.',0,5],
                "Wall" : ["|",0,0]
                }


def get_Gold_Rush_Elements():
    Elements = {}
    for key,value in elements_data.items():
        Elements[key] = Element(key,value[0],value[1],value[2])
    
    return Elements