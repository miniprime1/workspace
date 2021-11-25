from gtts import gTTS

print("Text2Speech v1.0 (TTS)")
print("Copyright (c) 2021 miniprime1")
print("[Powered by gTTS]\n")

path = input("Enter Save Path: ")
text = input("Enter Text: ")
lang = input("Enter Language: ")

if lang=="": lang="en"

try:
    tts = gTTS(text, lang=lang)
    tts.save(path)
    print("\nDone!")
except Exception as err:
    print("\nError:", str(err))

# Test Code
# from gtts import gTTS
# tts = gTTS("안녕하세요", lang="ko")
# tts.save("hi_kor.mp3")

# Note
# Language must be Country code
# Example: english=en; korean=ko