import datetime
import time
import locale

date = datetime.datetime.now()
locale.setlocale(locale.LC_TIME, "nl_NL")

print("Hello You! I am Dion.")
time.sleep(1)
print("Who are you?")
naam = input()
print("Hello " + naam + ".")
time.sleep(1)

print ("Ik ben een nieuwkomer op het Mediacollege Amsterdam door een aantal vragen over mij te beantwoorden leer je mij beter kennen")
time.sleep(1)

print("Voordat ik op het MBO op het Mediacollege Amsterdam kwam zat ik op school in")
print("A. Amsterdam")
print("B. Hoofddorp")
print("C. Haarlem")

question1 = input ("kies tussen A, B of C;")
if question1.lower() == "b":
    time.sleep(1)
    print("Correct!")
    time.sleep(2)
else:
    print("Incorrect, probeer het opnieuw")
    exit()

print("Goed gedaan, op naar de volgende vraag")
time.sleep(1.5)
print("In mijn vrije tijd doe ik aan")
print("A. Skaten")
print("B. Gamen")
print("C. Voetbal")

question2 = input ("kies tussen A, B of C;")
if question2.lower() == "a":
    time.sleep(1)
    print("Correct!")
    time.sleep(2)
else:
    print("Incorrect, probeer het opnieuw")
    exit()

print("Prima werk! Nog maar 2 vragen!")
time.sleep(1.5)
print("Ik ben .. jaar oud.")
print("A. 17")
print("B. 18")
print("C. 16")

question3 = input ("kies tussen A, B of C;")
if question3.lower() == "a":
    time.sleep(1)
    print("Correct!")
    time.sleep(2)
else:
    print("Incorrect, probeer het opnieuw")
    exit()

print("Prima werk!")
time.sleep(1.5)
print("Mijn favorite eten is ...")
print("A. Pizza shoarma")
print("B Pasta met pesto")
print("C. Nasi")

question4 = input ("kies tussen A, B of C;")
if question4.lower() == "b":
    time.sleep(1)
    print("Correct!")
    time.sleep(2)
else:
    print("Incorrect, probeer het opnieuw")

print("Goed gedaan! Je hebt alle vragen goed beantwoord")
