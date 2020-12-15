import math

import requests
from bs4 import BeautifulSoup


source = requests.get("https://www.mackolik.com/puan-durumu/t%C3%BCrkiye-s%C3%BCper-lig/2019-2020/482ofyysbdbeoxauk19yg7tdt").text

soup = BeautifulSoup(source,"lxml")





class Team:
    __slots__ = ["name","win","lose","tie","elo"]

    def __init__(self,name,win,lose,tie,elo):
        self.name = name
        self.win = win
        self.lose = lose
        self.tie = tie
        self.elo = 20 + elo

def Calculate(n,x):
    exp = (x - n) / 400.0
    return 1 / ((10.0 ** (exp)) + 1)

def eloProbablitiy(Team_0, Team_1):

    print(Team_0.name , "karşı" , Team_1.name , "elo algoritmasına göre kazanma şansı" ,Calculate(Team_0.elo,Team_1.elo))
    print( "------------------------------------------------------------------------------------------------------------------------------")
def Combination(team):
    allMatches = int(team.win) + int(team.lose) + int(team.tie)
    allMatchesCombined = 1
    winsCombined = 1
    tiesCombined = 1

    winRatio = float(float(team.win) / allMatches)
    TieRatio = float(float(team.tie) / allMatches)

    for i in range(1,int(allMatches)):
        allMatchesCombined *= i
    for i in range(1,int(team.win)):
        winsCombined *= i
    for i in range (1, int(team.tie)):
        tiesCombined *= 1
    ChanceOfWinning = (allMatchesCombined / winsCombined) * (winRatio ** int(team.win)) * ((1 - winRatio) ** int(team.lose)) * (winRatio)
    ChanceOfTie = (allMatchesCombined / tiesCombined) * (TieRatio ** int(team.tie)) * ((1- TieRatio) ** int(team.tie)) * (TieRatio)
    print(team.name , "oynayacağı" , str(allMatches) + "." , "maçın kazanacağı " , team.win + "." , "maç olmasının binom dağılıma göre olasılığı " + str(10000000000000000.0 /round(ChanceOfWinning, 2)))
    print("------------------------------------------------------------------------------------------------------------------------------")
    print(team.name, "oynayacağı", str(allMatches) + ".", "maçın berabere kalacağı  ", team.tie + ".", "maç olmasının binom dağılıma göre olasılığı " + str(10000000000000000.0 /round(ChanceOfTie, 2)))
    print("------------------------------------------------------------------------------------------------------------------------------")

teamArr = []
for divs in soup.find_all("table",class_="p0c-competition-tables__table p0c-competition-tables__table--total"):
    data = divs.tbody.text.split()
    data.remove("FK")
    data.remove("Yeni")
    data.remove("Ç.")
    data.remove("MKE")
    nameIndex = 2
    winIndex = 6
    tieIndex = 7
    loseIndex = 8
    for index in range(0,18):
        teamArr.append(Team(data[nameIndex], data[winIndex], data[loseIndex], data[tieIndex] , (int(data[winIndex]) *3) + (int(data[tieIndex]) * 1) + int(data[loseIndex]) * -2))
        nameIndex += 18
        winIndex += 18
        tieIndex += 18
        loseIndex += 18

for x , all in enumerate(teamArr,start = 1):
    print(x , all.name , "| Elo puanı :", all.elo)

print()
vs1 = input("Karşılaştırılacak ilk takım: ")
vs2 = input("Karşılaştırılacak ikinci takım: ")

index1 = 0
index2 = 0
found1 = False
found2 = False


for index in range(0,18):

    if (vs1 == teamArr[index].name):
        index1 = index
        found1 = True
    if (vs2 == teamArr[index].name):
        index2 = index
        found2 = True
    if(found1 == True and found2 == True):
        eloProbablitiy(teamArr[index1], teamArr[index2])
        Combination(teamArr[index1])
        Combination(teamArr[index2])
       

        break

if(found1 == False or found2 == False):
        print("Takım isimlerini doğru girdiğinizden emin olun")

