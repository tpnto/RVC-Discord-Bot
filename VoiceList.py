# --------------------Lista de Voces--------------------#


# you will put the voices available in your "voces" folder here
Voices = [

# your list of voices will go here! 
# make sure it's in this order:
# "Voice1", "Voice2", "Voice3"

]

# the path for your voice models will go here!

voice_paths = {
	# it should follow this structure
	#"Voice1": "voces/Voice1.pth",
	#"Voice2": "voces/Voice2.pth",
	#"Voice3": "voces/Voice3.pth"
}

# ------you dont change anything from now on :) -------#


# this function will check if any of the voices provided are available in voice_paths

def checarvoz(voz):
    rvc_voice = voice_paths.get(voz)
    return rvc_voice

# ------------------Columna-Help-----------------------#
def voicelist():
    num_rows = (len(Voices) + 1) // 2
    filas = []
    for i in range(num_rows):
        izquierda = Voices[i * 2]
        derecha = Voices[i * 2 + 1] if (i * 2 + 1) < len(Voices) else ""
        fila = f"{izquierda:<20}{derecha}"
        filas.append(fila)
    vocesdispo = '\n'.join(filas)
    listadevoces = f"```\n{vocesdispo}\n```"
    return listadevoces
