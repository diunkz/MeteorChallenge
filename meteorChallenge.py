# Junkes Queiroz Maia Junior

import cv2
from matplotlib import pyplot as plt


def convertImageBGRToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def showImage(img):
    plt.imshow(img)
    plt.show()


def getColor(img, y, x):
    return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)


def main():
    img = cv2.imread("meteor_challenge_01.png")
    img = convertImageBGRToRGB(img)
    stars = (255, 255, 255)  # pure white
    meteors = (255, 0, 0)  # pure red
    water = (0, 0, 255)  # pure blue
    qtstars = 0
    qtmeteors = 0
    coordWater = []
    meteorsFallingWater = 0
    findWaterLevel = False
    pixelsWaterLevel = []
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            red, green, blue = getColor(img, y, x)

            if tuple([red, green, blue]) == stars:
                qtstars += 1
            elif tuple([red, green, blue]) == meteors:
                qtmeteors += 1
            elif tuple([red, green, blue]) == water:
                coordWater.append(list([y, x]))
            if not findWaterLevel and tuple([red, green, blue]) == water:
                findWaterLevel = True
                waterLevel = y

    # descobrindo qual o nível da água
    for x in range(img.shape[1]):
        red, green, blue = getColor(img, waterLevel, x)
        if tuple([red, green, blue]) == water:
            pixelsWaterLevel.append(x)

    for y in range(waterLevel-1):
        for x in range(img.shape[1]):
            red, green, blue = getColor(img, y, x)
            if x in pixelsWaterLevel and tuple([red, green, blue]) == meteors:
                meteorsFallingWater += 1

    print(f"Image dimensions: {img.shape[1]}x{img.shape[0]}.")
    print(f"Number of stars: {qtstars}.")
    print(f"Number of meteors: {qtmeteors}.")
    print(f"Meteors that will fall on the water: {meteorsFallingWater}.")


main()
