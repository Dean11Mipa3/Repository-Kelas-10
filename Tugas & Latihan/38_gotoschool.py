

hadShower = True
hasBackpack = True

hasMeal = True
hasDuit = False

isSunday = False

shouldGoToSchool = not isSunday and (hadShower and hasBackpack) and (hasMeal or hasDuit)
print(shouldGoToSchool)