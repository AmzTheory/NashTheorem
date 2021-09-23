from itertools import product
from typing import Iterable

class Player():
    def __init__(self,id,actions,strategy) -> None:
        self.actions=actions
        self.strategy=strategy
        self.id=id
        self.utility=dict()
        ##nested dicts
        for act in self.actions:
            self.utility[act]=dict()

    def Actions(self):
        return self.actions

    # def Utility(self,opp,act,oppact):
    #     return self.actions[act]

    def Strat(self,act):
        return self.strategy[act]

    def Update(self,strat):
        self.strategy=strat

    def setUtility(self,opp,act,oppact,value):
        key=str(opp.id)+oppact
        self.utility[act][key]=value

    def Utility(self,opp,act,oppact):
        key=str(opp.id)+oppact
        return self.utility[act][key]

    def __hash__(self) -> int:
        return self.id

    def __eq__(self, o: object) -> bool:
        if o is not None:
            return self.id==o.id
        
        return False

  
class Game():
    def __init__(self,pls) -> None:
        self.pls=pls
        

    def UtilityForAction(self,pl,opp,act):
        # sumproduct=opp.Strat(act)
        
        # for a,v in opp.strat():
        #     st=opp.strat()
        #     sumproduct*=st[act]
        res=0
        for oppact in opp.Actions():
            # print(act,oppact,pl.Utility(opp,act,oppact),"*",(opp.Strat(oppact)))
            res+=pl.Utility(opp,act,oppact)*(opp.Strat(oppact))

        return res

    def possibleActions(self):
        return product(self.pls[0].Actions(),self.pls[1].Actions())
    def expectedUtility(self,pl):
        value=0
        opp=filter(lambda x:x.id != pl.id,self.pls)[0]
        for act,actopp in self.possibleActions():
            sumproduct=0
            for p in self.pls:
                sumproduct*=p.Strat(self.profile[pl])
            
            # for act1,act2 in self.possibleActions():
            #     pl.


            value+=pl.Utility(opp,act,actopp)*sumproduct

    def mixedStrategyWithout(self,pl):
        filtered=filter(lambda p:p!=pl,self.pls)
        return list(filtered)
    def computePhi(self,a,b):
        return max(0,a-b)
    def computeUtilitiesForallActions(self,pl):
        uts=dict()
        opp=self.mixedStrategyWithout(pl)[0]
        sum=0
        actions=pl.Actions()
        for act in actions:
            value=self.UtilityForAction(pl,opp,act)
            uts[act]=value
            sum+=value

        ui=0
        for act,value in uts.items():
            ui+=pl.Strat(act)*uts[act]
        return uts,ui

    def computePhiForPlayer(self,pl):
        uts,avg=self.computeUtilitiesForallActions(pl)
        phi={}
        # print(uts,avg)
        for act in pl.Actions():
            phi[act]=self.computePhi(uts[act],avg)
        return phi
    def updateStrategy(self,pl,phi):
        newStrat=dict()
        su=(1+sum(phi.values()))
        for act,p in phi.items():
            newStrat[act]=round((pl.Strat(act)+ phi[act])/su,5)
        return newStrat
    def updateStrategies(self):
        newStrategies=dict()
        for pl in self.pls:
            phi=self.computePhiForPlayer(pl)
            # print(phi)
            newStrategies[pl]=self.updateStrategy(pl,phi)
        return newStrategies
    def update(self,strategies):
        for pl in self.pls:
            strat=strategies[pl]
            pl.Update(strat)






def findSol(game:Game):
     updated=game.updateStrategies()
     print([v for p,v in updated.items()])
     for pl in game.pls:
         for act in pl.Actions():
             if updated[pl][act] != pl.Strat(act):
                 game.update(updated)
                 return findSol(game)

     return [p.strategy for p in game.pls]

# pl1=Player(id=1,actions=["a","b"],strategy={"a":0.5,"b":0.5})
# pl2=Player(id=2,actions=["a","b"],strategy={"a":0.25,"b":0.75})
# game=Game([pl1,pl2])
# pl1.setUtility(pl2,"a","a",2)
# pl1.setUtility(pl2,"a","b",0)
# pl1.setUtility(pl2,"b","a",0)
# pl1.setUtility(pl2,"b","b",1)

# pl2.setUtility(pl1,"a","a",1)
# pl2.setUtility(pl1,"a","b",0)
# pl2.setUtility(pl1,"b","a",0)
# pl2.setUtility(pl1,"b","b",2)

pl1=Player(id=1,actions=["a","b","c"],strategy={"a":0.5,"b":0.5,"c":0})
pl2=Player(id=2,actions=["a","b","c"],strategy={"a":0.5,"b":0,"c":0.5})

pl2=Player(id=1,actions=["a","b","c"],strategy={"a":0.5,"b":0.5,"c":0})
pl1=Player(id=2,actions=["a","b","c"],strategy={"a":0.5,"b":0,"c":0.5})

game=Game([pl1,pl2])
pl1.setUtility(pl2,"a","a",3)
pl1.setUtility(pl2,"a","b",3)
pl1.setUtility(pl2,"a","c",0)
pl1.setUtility(pl2,"b","a",4)
pl1.setUtility(pl2,"b","b",0)
pl1.setUtility(pl2,"b","c",1)
pl1.setUtility(pl2,"c","a",0)
pl1.setUtility(pl2,"c","b",4)
pl1.setUtility(pl2,"c","c",5)

pl2.setUtility(pl1,"a","a",3)
pl2.setUtility(pl1,"a","b",4)
pl2.setUtility(pl1,"a","c",0)
pl2.setUtility(pl1,"b","a",3)
pl2.setUtility(pl1,"b","b",0)
pl2.setUtility(pl1,"b","c",4)
pl2.setUtility(pl1,"c","a",0)
pl2.setUtility(pl1,"c","b",1)
pl2.setUtility(pl1,"c","c",5)


print(pl1.utility)
print(pl2.utility)

# print([i.id for i in game.mixedStrategyWithout(pl1
# pi=game.computePhiForPlayer(pl1)
print(findSol(game))