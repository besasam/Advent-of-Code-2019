def makeImage(data, width, height):
    layerSize = width * height
    numOfLayers = int(len(data) / layerSize)
    image = []
    pos = 0
    for l in range(0, numOfLayers):
        layer = []
        for h in range(0, height):
            layer.append(data[pos * width:(pos + 1) * width])
            pos += 1
        image.append(layer)
    return image


def countCharactersInLayer(layer, character):
    count = 0
    for row in layer:
        count += row.count(str(character))
    return count


data = open('input.txt').read()
image = makeImage(data, 25, 6)
fewestZeros = 25 * 6
fewestZeroLayer = None

for layer in image:
    zeroCount = countCharactersInLayer(layer, 0)
    if zeroCount < fewestZeros:
        fewestZeros = zeroCount
        fewestZeroLayer = layer

res = countCharactersInLayer(fewestZeroLayer, 1) * countCharactersInLayer(fewestZeroLayer, 2)
print(res)