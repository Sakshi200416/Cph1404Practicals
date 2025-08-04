from guitar import Guitar
from musician import Musician
from band import Band


def main():
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.00))

    gary = Musician("Gary Cherone")

    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))

    kevin = Musician("Kevin Figueiredo")

    extreme = Band("Extreme")
    extreme.add(nuno)
    extreme.add(gary)
    extreme.add(pat)
    extreme.add(kevin)

    print(extreme)
    print("band.play()")
    extreme.play()


if __name__ == '__main__':
    main()
