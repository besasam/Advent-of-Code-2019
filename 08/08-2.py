def makeImage(data, width, height):
    layerSize = width * height
    numOfLayers = int(len(data) / layerSize)
    image = []
    pos = 0
    for l in range(0, numOfLayers):
        layer = []
        for h in range(0, height):
            layer.append([int(x) for x in data[pos * width:(pos + 1) * width]])
            pos += 1
        image.append(layer)
    return image


def decodeImage(image):
    width = len(image[0][0])
    height = len(image[0])
    layers = len(image)
    res = []
    for row in range(0, height):
        currentrow = []
        for column in range(0, width):
            pixel = None
            i = 0
            while pixel is None:
                if i == layers - 1:
                    pixel = 2
                if image[i][row][column] != 2:
                    pixel = image[i][row][column]
                i += 1
            currentrow.append(pixel)
        res.append(currentrow)
    return res


def printImage(image):
    for row in image:
        currentrow = ''
        for pixel in row:
            if pixel == 0:
                currentrow += '█'
            else:
                currentrow += ' '
        print(currentrow)


data = open('input.txt').read()
image = makeImage(data, 25, 6)
printImage(decodeImage(image))