import plotly.express as px

# Do not modify the line below.
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
colors = ["blue", "green", "red", "yellow"]

dictCountries = {
    "Argentina": ["Bolivia", "Brazil", "Chile", "Paraguay", "Uruguay"],
    "Bolivia": ["Argentina", "Brazil", "Chile", "Paraguay", "Peru"],
    "Brazil": ["Argentina", "Bolivia", "Colombia", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"],
    "Chile": ["Argentina", "Bolivia", "Peru"],
    "Colombia": ["Brazil", "Ecuador", "Peru", "Venezuela"],
    "Ecuador": ["Colombia", "Bolivia", "Peru"],
    "Falkland Islands": [],
    "Guyana": ["Brazil", "Suriname", "Venezuela"],
    "Paraguay": ["Argentina", "Bolivia", "Brazil"],
    "Peru": ["Bolivia", "Brazil", "Chile", "Colombia", "Ecuador"],
    "Suriname": ["Brazil", "Guyana"],
    "Uruguay": ["Argentina", "Brazil"],
    "Venezuela": ["Brazil", "Colombia", "Guyana"]
    }


def sort(unSortedCountries):
    newCountry = {}
    retCountries = []
    for country in unSortedCountries:
        newCountry.update({country: len(dictCountries[country])})

    newCountry = list(sorted(newCountry.items(), key=lambda kv: kv[1]))

    i = len(newCountry) - 1
    while i > -1:
        retCountries.append(newCountry[i][0])
        i -= 1

    return retCountries


def isColoredTheTrue(testMap):
    for node in dictCountries:
        edges = (dictCountries[node])
        colorOfNode = testMap[node]
        for edge in edges:
            colorOfEdge = testMap[edge]
            if colorOfNode == colorOfEdge:
                return False
    return True


def colorTheCountry(Map, dictCountry):
    sortedCountries = sort(dictCountry)
    a = 3
    x = 0
    clrCounter = 0
    isSolved = True
    while x < len(sortedCountries):
        if clrCounter == len(colors):
            print("Unsolved Problem")
            isSolved = False
            break
        tmpx = x
        Map.update({sortedCountries[x]: colors[a]})
        if not isColoredTheTrue(Map):
            x -= 1
        if a < 3:
            a += 1
        else:
            a = 0
        x += 1
        if tmpx == x: clrCounter += 1
        else: clrCounter = 0
    return Map, isSolved


# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.

def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}
    if isColoredTheTrue(colormap_test):
        print("colors of colormap_test is true.")
    else:
        print("colors of colormap_test is false.")
    solution = {}
    for i in range(len(countries)):
        solution.update({countries[i]: f"color_{i}"})

    newMap, isTrue = colorTheCountry(solution, countries)
    if isTrue:
        print("colors of newMap is true.")
        plot_choropleth(colormap=newMap)
    else:
        print("colors of newMap is false.")

