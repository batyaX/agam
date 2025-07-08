from telethon import TelegramClient, events
import random
import os

# === Ortam Değişkenlerinden API Bilgileri ===
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
bot_token = os.environ['BOT_TOKEN']

client = TelegramClient('keyword_bot', api_id, api_hash).start(bot_token=bot_token)

yanitlar = {
    "vpn": [
        "vpn üçin şulara yüz tutyn: @User_bruh,@montrex77,@Loner_8,@assassincreed_official.",
        "@User_bruh şul agamda gowja vpnler bar oytyan.",
        "@montrex77 vpn diysen şul user kella gelibermeli.",
        "@Loner_8 amatly baha diysen hem köp bolar, muna döwüük baha diyibermeli.",
        "vpn aljak bolsan şuna yüz tut @assassincreed_official.",
        "Mugyt Vipiyen gözleyan bolson şul kanalda yada https://t.me/St4rvpn şutayda bardyr hökmany yagdayda.",
        "vpn diydinmi, o name zat iyilyan zamy :D.",
        "menem bilyan sana vpn gerekdigini."
    ],
    "star": [
        "glavny başlyk @st4rland.",
        "birisi star sözünü ulandy öytyan, men dine starlar hakkynda şuny bilyan https://t.me/St4rvpn https://t.me/turkmen2025 .",
        "star diymek yyldyz diymek.",
        "işin düşse şuna yüzlen @s4rland .",
        "star diydinmi, haysy star hakda gürleyan @st4rland ."
    ],
    "decrypt": [
        "decrypt diysen şul başda kanal kella gelya https://t.me/turkmen2025",
        "decryptor bolmagam kyndyr dossym",
        "decrypt üçin yüz tutay @st4rland",
        "decrypt etmeli bolsa kanaldaky adminler göni eder, alada etme."
    ],
    "batyr": [
        "oyn etmayda batyr"
    ]
}

kelime_haritasi = {
    "vpn": ["vpn"],
    "star": ["star", "st4r", "starland", "st4rland"],
    "decrypt": ["decrypt", "decryptor"],
    "batyr": ["batyr"]
}

@client.on(events.NewMessage)
async def handle_keyword(event):
    if not event.is_group:
        return
    mesaj = event.raw_text.lower()
    for anahtar, varyasyonlar in kelime_haritasi.items():
        if any(k in mesaj for k in varyasyonlar):
            secilen_yanit = random.choice(yanitlar[anahtar])
            await event.reply(secilen_yanit)
            break

print("Bot sadece gruplarda çalışacak şekilde başlatıldı.")
client.run_until_disconnected()
