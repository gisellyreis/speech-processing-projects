import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

def record_text():
  # loop in case of errors
  while(1):
    try:
      # use the microphone as source for input.
        with sr.Microphone() as source2:
             
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input 
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
            return MyText
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")

  return

def output_text(text):
  f = open("output.txt", "a")
  f.write(text)
  f.write("\n")
  f.close()
  print(text)
  return

while(1):
  text = record_text()
  output_text(text)

  print("I wrote what you said.")