import entities.energy
class VictoryPoints:

    CONSTRUCTIVE = 1
    INVERTIBLE = 2
    GENERATIVE = 3
    PRIMAL = 4
    def calcFullyGainedEnergy(engine,player):
        gainableEnergyList = []
        fullyGainedEnergy = 0
        vp_allocation = { 
            1: 3,
            2: 6,
            3: 10,
            4: 15
        }
        if (gainableEnergyList.count(Energy.CONSTRUCTIVE) == 0):
            fullyGainedEnergy += 1
        if (gainableEnergyList.count(Energy.INVERTIBLE) == 0):
            fullyGainedEnergy += 1
        if (gainableEnergyList.count(Energy.GENERATIVE) == 0):
            fullyGainedEnergy += 1
        if (gainableEnergyList.count(Energy.PRIMAL) == 0):
            fullyGainedEnergy += 1
        vp_points = vp_allocation.get(fullyGainedEnergy)
        return vp_points
    
    def calcMonumentEnergy(engine,player):
        monumentList = []
        vp_points = 0
        vp_allocation = {
            1: 3,
            2: 7,
            3: 12,
            4: 12
        }
        for i in monumentList(engine,player):
            num_energy = 0
            for j in i.energyList:
                if (j.owner == player):
                    num_energy+= 1
            vp_points += vp_allocation.get(num_energy)
        return vp_points

    
    def calcPillars(engine,player):
        vp_allocation = {
                1: 3,
                2: 8,
                3: 14,
                4: 21,
                5: 29,
                6: 38
            }
        num_tiles = 0
        for pillar in pillarList:  #insert pillar engine command here
            for tile in pillar.tiles:
                if (tile.owner == player):
                    num_tiles += 1
        vp_points = vp_allocation.get(num_tiles)
        return vp_points

    def calcAchievements(engine,player):
        #insert constants
        vp_points = 1
        return vp_points



