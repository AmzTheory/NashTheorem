from script import Game,Player,findSol


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

#print utilities
# print(pl1.utility)
# print(pl2.utility)



print(findSol(game))