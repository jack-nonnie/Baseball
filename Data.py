import pandas as pd
import numpy as np
from scipy import stats

asBattingData = pd.read_csv("As_batting.csv")
astrosBattingData = pd.read_csv("Astros_batting.csv")
bluejaysBattingData = pd.read_csv("Bluejays_batting.csv")
bravesBattingData = pd.read_csv("Braves_batting.csv")
brewersBattingData = pd.read_csv("Brewers_batting.csv")
cardinalsBattingData = pd.read_csv("Cardinals_batting.csv")
cubsBattingData = pd.read_csv("Cubs_batting.csv")
diamondbacksBattingData = pd.read_csv("Diamondbacks_batting.csv")
dodgersBattingData = pd.read_csv("Dodgers_batting.csv")
giantsBattingData = pd.read_csv("Giants_batting.csv")
indiansBattingData = pd.read_csv("Indians_batting.csv")
marinersBattingData = pd.read_csv("Mariners_batting.csv")
metsBattingData = pd.read_csv("Mets_batting.csv")
nationalsBattingData = pd.read_csv("Nationals_batting.csv")
oriolesBattingData = pd.read_csv("Orioles_batting.csv")
padresBattingData = pd.read_csv("Padres_batting.csv")
philliesBattingData = pd.read_csv("Phillies_batting.csv")
piratesBattingData = pd.read_csv("Pirates_batting.csv")
rangersBattingData = pd.read_csv("Rangers_batting.csv")
redsBattingData = pd.read_csv("Reds_batting.csv")
redsoxBattingData = pd.read_csv("Redsox_batting.csv")
rockiesBattingData = pd.read_csv("Rockies_batting.csv")
royalsBattingData = pd.read_csv("Royals_batting.csv")
tigersBattingData = pd.read_csv("Tigers_batting.csv")
twinsBattingData = pd.read_csv("Twins_batting.csv")
whitesoxBattingData = pd.read_csv("Whitesox_batting.csv")
yankeesBattingData = pd.read_csv("Yankees_Batting.csv")

columns = astrosBattingData.columns
listOfDf = [asBattingData, astrosBattingData,bluejaysBattingData, bravesBattingData, brewersBattingData, cardinalsBattingData, cubsBattingData, diamondbacksBattingData, dodgersBattingData,giantsBattingData,indiansBattingData, marinersBattingData, metsBattingData, nationalsBattingData, oriolesBattingData, padresBattingData, philliesBattingData, piratesBattingData, rangersBattingData, redsBattingData, redsoxBattingData, rockiesBattingData, royalsBattingData, tigersBattingData, twinsBattingData, whitesoxBattingData, yankeesBattingData]
def listMaker(col, year):
    lst= np.array([])
    for df in listOfDf:
        yearStat = df[df.Year == year]
        lst = np.append(lst, yearStat[col])
    return lst
list =listMaker("W", 2018)
print(columns)
print(list)
print(stats.zscore(list))
def yearDfMaker(year):
    adjustDf = pd.DataFrame([], columns=["Team", "W", "L", "R/G", "G", "PA", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB", "CS", "BB", "SO", "BA", "OBP", "SLG", "OPS", "E", "DP", "Fld%"])
    adjustDf.Team = ["As", "Astros", "Blue_Jays", "Braves", "Brewers", "Cardinals", "Cubs", "Diamondbacks", "Dodgers", "Giants", "Indians", "Mariners", "Mets", "Nationals", "Orioles", "Padres", "Phillies", "Pirates", "Rangers", "Reds", "Red_Sox", "Rockies", "Royals", "Tigers", "Twins", "White_Sox", "Yankees"]
    adjustDf.W = stats.zscore(listMaker("W", year))
    adjustDf.L = stats.zscore(listMaker("L", year))
    adjustDf["R/G"] = stats.zscore(listMaker("R/G", year))
    adjustDf.G = listMaker("L", year)
    adjustDf.PA = stats.zscore(listMaker("PA", year))
    adjustDf.AB = stats.zscore(listMaker("AB", year))
    adjustDf.R = stats.zscore(listMaker("R", year))
    adjustDf.H = stats.zscore(listMaker("H", year))
    adjustDf["2B"] = stats.zscore(listMaker("2B", year))
    adjustDf["3B"] = stats.zscore(listMaker("3B", year))
    adjustDf.HR = stats.zscore(listMaker("HR", year))
    adjustDf.RBI = stats.zscore(listMaker("RBI", year))
    adjustDf.SB = stats.zscore(listMaker("SB", year))
    adjustDf.CS = stats.zscore(listMaker("CS", year))
    adjustDf.BB = stats.zscore(listMaker("BB", year))
    adjustDf.SO = listMaker("SO", year)
    adjustDf.BA = stats.zscore(listMaker("BA", year))
    adjustDf.OBP = stats.zscore(listMaker("OBP", year))
    adjustDf.SLG = stats.zscore(listMaker("SLG", year))
    adjustDf.OPS = stats.zscore(listMaker("OPS", year))
    adjustDf.E = stats.zscore(listMaker("E", year))
    adjustDf.DP = stats.zscore(listMaker("DP", year))
    adjustDf["Fld%"] = stats.zscore(listMaker("Fld%", year))
    print(adjustDf)
    return True



sumData = pd.DataFrame( [], columns= columns)
sumData.Year = astrosBattingData.Year
sumData.W = astrosBattingData.W + asBattingData.W
yearDfMaker(2019)
