# importamos librerias , buscar como migrar al robot
import speech_recognition as sr_dime
import pyttsx3, pywhatkit


name = "pica"  # nombre del asistente 
engine = pyttsx3.init() # lo vamos a usar para buscar las voces dentro del O.S
voices = engine.getProperty("voices")
#for i in voices:
#    print(i)
engine.setProperty("voices", voices[0].id) #Tomamos la voz de la posicion 0  de la cantdad de voces que tiene el O.S



#funcion para charlar
def talk(some_text):
    engine.say(some_text)
    engine.runAndWait()
    
def listen():
    escuchar = sr_dime.Recognizer()
    try:
        with sr_dime.Microphone() as source:
            print(" Procesando lo que dijiste...")
            escuchar.adjust_for_ambient_noise(source)
            # va ejecutar
            pc = escuchar.listen(source)
            rec = escuchar.recognize_google(pc, language="es")
            rec = rec.lower()
            #talk(rec)
    except sr_dime.UnknownValueError:
        print(" No entendi lo que dijiste, repitelo")
    return rec

def buscar():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            talk("No te entendi, intenta de nuevo porfi")
            continue
        if name in rec:
            rec = rec.replace(name, '').strip()
            if 'reproduce' in rec:
                song = rec.replace('reproduce', '').strip()
                pywhatkit.playonyt(song)
                talk(f"Reproduciendo {song}.")
        

if __name__ == '__main__':
    buscar()