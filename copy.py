def isMeetEnemy(listOfPlayerBullets, listOfEnemies):
    toDelete = []
    for playerBullet in listOfPlayerBullets:
        positionOfBulletPlayer = canvas.coords(playerBullet)        
        for enemy in listOfEnemies:
            positionOfEn = canvas.coords(enemy)            
            if (positionOfBulletPlayer[1] <= positionOfEn[1]+20) and (((positionOfBulletPlayer[0] >= positionOfEn[0]) and (positionOfBulletPlayer[0] <= positionOfEn[0]+55)) or ((positionOfBulletPlayer[0]+15 >= positionOfEn[0]) and (positionOfBulletPlayer[0]+15 <= positionOfEn[0]+55))):
                toDelete.append(playerBullet)
                toDelete.append(enemy)
                winsound.PlaySound("sound/explosion.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    return toDelete