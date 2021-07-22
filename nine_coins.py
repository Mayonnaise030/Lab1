import random
class Nine_Coins:
    #The _ _init_ _ method initializes the upperside data attribute with 'Tails'.
    def __init__(self, num):
        self.binary = bin(num)[2:].zfill(9) # 定義物件的binary
        self.decimal = num                  # 定義物件的decimal
        Nine_Coins = ""
        for i in range(9):
            if self.binary[i] == "1":
                Nine_Coins += "T"
            elif self.binary[i] == "0":
                Nine_Coins += "H"
        self.Nine_Coins = Nine_Coins     # 定義物件的Nine_Coins(用來存放含"H" "T"的str)
    # 定義toss
    def toss(self):
        gamer_type = ["H","T"]           # 建立含"H" "T"的array
        HT_temp = ""                     # 建立存放"H" "T"的str
        Binary_temp = ""                 # 建立存放"0" "1"的str
        for i in range(9):
            HT_temp = HT_temp + gamer_type[random.randint(0, 1)]  # 隨機存放"H" "T"到 HT_temp
            # 存放"0" "1"到 Binary_temp
            if HT_temp[i] == "H":
                Binary_temp += "0"
            elif HT_temp[i] == "T":
                Binary_temp += "1"
        self.binary = Binary_temp               # 定義物件的binary
        self.decimal = int(Binary_temp, 2)      # 定義物件的decimal
        self.Nine_Coins = HT_temp               # 定義物件的Nine_Coins
    def __str__(self):   # 定義物件的字串描述
        return f'binary: {self.binary} and decimal : {self.decimal}'      
    def __repr__(self):  # 定義物件的representation
        return (f'Nine_Coins :"'+  self.Nine_Coins +'"')




