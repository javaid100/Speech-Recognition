# =============== For Voice ================================

import pyttsx3
voiceEngine = pyttsx3.init()


def Speak (string, id):
    if id == 0:
        male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
        voiceEngine.setProperty('voice', male_voice_id)
        voiceEngine.setProperty('rate', 125)
        voiceEngine.setProperty('volume', 1)
        voiceEngine.say(string)    
        voiceEngine.runAndWait()
    if id == 1:
        fem_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        voiceEngine.setProperty('voice', fem_voice_id )
        voiceEngine.setProperty('rate', 125)
        voiceEngine.setProperty('volume', 1)
        voiceEngine.say(string)
        voiceEngine.runAndWait()

# ==========================================================
