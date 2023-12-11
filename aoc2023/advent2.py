def parseData(content):
    games = content.strip().split('\n')

    parseData = []

    maxRed = 15
    maxBlue = 16
    maxGreen = 17

    #I can enum and add the index to an array then just add up the indexes in the array
    for game in games:
        gameNumber, pairs = game.split(':')

        #gameData = {'gameNumber': int(gameNumber.strip())}

        print(gameNumber)
        print(pairs)

def main():    
    filePath = "C:\\cygwin64\\home\\cicyf\\aaron\\pyfun\\aoc2023\\advent2.txt"

    with open(filePath, "r") as file:
        content = file.read()
    
    parseData(content)

if __name__ == "__main__":
    main()