import json
from difflib import get_close_matches #import get_close_match dari difflib

data = json.load(open("kamus.json"))

def terjemahan(kata):
	kata = kata.lower()
	if kata in data:
		return data[kata]
	elif len(get_close_matches(kata, data.keys())) > 0: #cek apakah ada kata yang hampir mirip dengan input yang di berikan user
		yt = input("Apakah kata yang dimaksud adalah %s ? ketik Y jika iya, atau T jika Tidak: " % get_close_matches(kata, data.keys())[0]) # cek ke user apakah ini kata yang di maksud
		if yt == "Y":
				return data[get_close_matches(kata, data.keys())[0]]
		elif yt == "T":
				return "kata tidak ada, silahkan di cek ulang"
		else:
			return "Kami tidak dapat mengerti input yang dimaksud"
	else:
		return "kata tidak ada, silahkan di cek ulang"

kata = input('masukan kata: ')

print(terjemahan(kata))
