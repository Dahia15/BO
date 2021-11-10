import time
import sys

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]

required = ("\n Gebruik alleen A, B, C of D \n")


def begin():
    print("Er is oorlog uitgebroken in Nederland en het land wordt bezet, het is hier niet veilig. Wat ga je doen?")
    print("A | Je vlucht met je famillie.")
    print("B | Je gaat schuilen.")
    print("C | Je gaat bij het verzet.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_vluchten()
    if choice in answer_B:
        option_niks()
    if choice in answer_C:
        option_verzet()
    else:
        print(required)
        begin()


def option_vluchten():
    print("De bezetters stormen binnen en ze willen je oppakken. Wat ga je doen?")
    print("A | Je gaat vluchten.")
    print("B | Je geeft je over.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_vluchten2()
    if choice in answer_B:
        print("De bezetters logen en schieten je neer in je huis. Je bent dood")
        sys.exit()
    else:
        print(required)
        option_vluchten()


def option_vluchten2():
    print("Je hebt er voor gekozen om te vluchten, je hebt een aantal opties op de manier hoe je vlucht.")
    print("A | Je gaat met de auto naar Italië.")
    print("B | Je gaat met de boot naar England.")
    print("C | Je gaat met de auto naar Turkijë.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortitalie()
    if choice in answer_B:
        option_paspoortengland()
    if choice in answer_C:
        option_paspoortturkije()
    else:
        print(required)
        option_vluchten2()


def option_paspoortitalie():
    print("Om het land binnen te komen heb je een paspoort nodig. Heb je die mee?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeeitalie()
    if choice in answer_B:
        print("Je hebt je paspoort niet meegenomen. Je wordt opgepakt door de politie en je verhongerd in je cel.")
        sys.exit()
    else:
        print(required)
        option_paspoortitalie()


def option_paspoortmeeitalie():
    print("Je hebt je paspoort meegenomen en je bent veilig in Italië aangekomen. Je zoekt naar een manier om geld te verdienen.")
    time.sleep(1)
    print("Je begint te werken met de mafia en wordt opgepakt door de politie. Je krijgt 5 jaar celstraf.")
    time.sleep(5)
    print("Terwijl je in de cel zat was de oorlog in Nederland over")
    print("Je bent uit de gevangenis gekomen, Je krijgt een nieuw begin en zoekt naar een baan.")
    print("Je moet een beroep kiezen voor je toekomst.")
    print("A | Tandarts")
    print("B | Ziekenhuis manager")
    print("C | Accountant")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden. Je wordt overgeplaatst naar Nederland om daar verder te werken")
        time.sleep(1)
        print("Je gaat wonen in een mooi huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent ziekenhuis manager geworden. Ze hebben je nodig in Nederland voor belangrijke zaken.")
        time.sleep(1)
        print("Je gaat daar wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent Accountant geworden. Het bedrijf waar je werkt is falliet gegaan maar er zijn nieuwe kansen in Nederland")
        time.sleep(1)
        print("Je komt te overlijden door een vliegtuig ongeluk.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden. Je kan gaan werken bij Google in Amsterdam")
        time.sleep(1)
        print("Je gaat daar wonen in een prachtige villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_paspoortmeeitalie()


def option_niks():
    print("Je ziet dat mensen in je omgeving in het verzet gaan, je wilt iets doen. Wat ga je doen?")
    print("A | Je gaat in het verzet.")
    print("B | Je gaat vluchten.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Je hebt besloten om in het verzet te gaan. De overheid heeft je opgepakt en gemarteld tot de dood.")
        sys.exit()
    if choice in answer_B:
        option_vluchten2()
    else:
        print(required)
        option_niks()


def option_verzet():
    print("Je hebt besloten om in het verzet te gaan. De bezetters zoeken je en willen je dood hebben, wat doe je?")
    print("A | Je geeft je over.")
    print("B | Je vlucht.")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Je hebt er voor gekozen om jezelf over te geven. De bezetters hebbem je gevangen genomen en gemarteld. Je bent overleden.")
        sys.exit()
    if choice in answer_B:
        option_vluchten2()
    else:
        print(required)
        option_verzet()


def option_paspoortengland():
    print("Om het land binnen te komen heb je een paspoort nodig. Heb je die mee?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeeEngeland()
    if choice in answer_B:
        print("Je hebt je paspoort niet meegenomen. Je wordt opgepakt door de politie, ze gooien je in de gevangenis en je wordt gemarteld tot de dood.")
        sys.exit()
    else:
        print(required)
        option_paspoortengland()


def option_paspoortmeeEngeland():
    print("Je moet vanuit Engeland met het vliegtuig naar Griekenland.")
    print("Kies A of B")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_veiligGriekenland()
    if choice in answer_B:
        print("Het vliegtuig is gecrashd, je kan niet zwemmen en bent daardoor verdronken.")
        sys.exit()
    else:
        print(required)
        option_paspoortmeeEngeland()
        

def option_veiligGriekenland():
    print("Je bent veilig aangekomen in Griekenland en je begint te zoeken naar een manier om geld te verdienen.")
    time.sleep(1)
    print("Tijdens je lange rijs was de oorlog in Nederland over gegaan")
    time.sleep(2)
    print("Nu is het tijd om een beroep te kiezen.")
    print("A | Tandarts")
    print("B | Ziekenhuis manager")
    print("C | Accountant")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden. Je wordt overgeplaatst naar Nederland om daar verder te werken")
        time.sleep(1)
        print("Je gaat wonen in een mooi huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent ziekenhuis manager geworden. Ze hebben je nodig in Nederland voor belangrijke zaken.")
        time.sleep(1)
        print("Je gaat daar wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent Accountant geworden. Het bedrijf waar je werkt is falliet gegaan maar er zijn nieuwe kansen in Nederland")
        time.sleep(1)
        print("Je komt te overlijden door een vliegtuig ongeluk.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden. Je kan gaan werken bij Google in Amsterdam")
        time.sleep(1)
        print("Je gaat daar wonen in een prachtige villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_veiligGriekenland()


def option_paspoortturkije():
    print("Om het land binnen te komen heb je een paspoort nodig. Heb je die mee?")
    print("A | Ja")
    print("B | Nee")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        option_paspoortmeeturkije()
    if choice in answer_B:
        print("Je hebt je paspoort niet meegenomen. Je wordt opgepakt door de politie, ze zetten je terug op zee en je verhongerd daar.")
        sys.exit()
    else:
        print(required)
        option_paspoortturkije()


def option_paspoortmeeturkije():
    print("Je komt veilig binnen Turkije en begint te zoeken naar een manier om geld te verdienen.")
    time.sleep(1)
    print("Tijdens je lange rijs was de oorlog in Nederland over gegaan")
    time.sleep(2)
    print("Nu is het tijd om een beroep te kiezen.")
    print("A | Tandarts")
    print("B | Ziekenhuis manager")
    print("C | Accountant")
    print("D | Software Developer")
    time.sleep(1)
    choice = input('>>')
    if choice in answer_A:
        print("Gefeliciteerd! Je bent tandarts geworden. Je wordt overgeplaatst naar Nederland om daar verder te werken")
        time.sleep(1)
        print("Je gaat wonen in een mooi huis en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_B:
        print("Gefeliciteerd! Je bent ziekenhuis manager geworden. Ze hebben je nodig in Nederland voor belangrijke zaken.")
        time.sleep(1)
        print("Je gaat daar wonen in een flat en leeft lang en gelukkig.")
        sys.exit()
    if choice in answer_C:
        print("Gefeliciteerd! Je bent Accountant geworden. Het bedrijf waar je werkt is falliet gegaan maar er zijn nieuwe kansen in Nederland")
        time.sleep(1)
        print("Je komt te overlijden door een vliegtuig ongeluk.")
        sys.exit()
    if choice in answer_D:
        print("Gefeliciteerd! Je bent software developer geworden. Je kan gaan werken bij Google in Amsterdam")
        time.sleep(1)
        print("Je gaat daar wonen in een prachtige villa en je leeft lang en gelukkig.")
        sys.exit()
    else:
        print(required)
        option_paspoortturkije()


begin()