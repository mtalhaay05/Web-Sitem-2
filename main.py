from flask import Flask, render_template
import random
import string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/aboutus")
def about_us():
    return render_template("about.html")

@app.route("/bilgiler")
def random_bilgiler():
    facts_list = [
        "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
        "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
        "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50 den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."
    ]
    return f"<p>{random.choice(facts_list)}</p>"

@app.route("/yazi-tura")
def yazi_tura():
    sonuc = random.choice(["Yazı", "Tura"])
    return render_template("yazi_tura.html", sonuc=sonuc)

@app.route("/sifre")
def sifre_olusturucu():
    karakterler = string.ascii_letters + string.digits + "!@#$%&*"
    sifre = "".join(random.choice(karakterler) for _ in range(12))
    return render_template("sifre.html", sifre=sifre)

@app.route("/resim")
def rastgele_resim():
    resimler = [
        {
            "kategori": "Hayvan",
            "baslik": "Tatlı Bir Kedi",
            "url": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800"
        },
        {
            "kategori": "Uzay",
            "baslik": "Derin Uzay ve Yıldızlar",
            "url": "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=800"
        },
        {
            "kategori": "Meme",
            "baslik": "Klasik Kodlama Anı",
            "url": "https://i.imgflip.com/30b1gx.jpg"
        }
    ]
    secilen = random.choice(resimler)
    return render_template("resim.html", resim=secilen)

@app.route("/bilmece")
def bilmece():
    bilmeceler = [
        {
            "soru": "Ağzı var dili yok, konuşur ama sesi yok. Nedir?",
            "cevap": "Kitap"
        },
        {
            "soru": "Ben giderim o gider, arkamdan tin tin eder. Nedir?",
            "cevap": "Gölge"
        },
        {
            "soru": "Yer altında sakallı dede. Nedir?",
            "cevap": "Pırasa"
        }
    ]
    secilen_bilmece = random.choice(bilmeceler)
    return render_template("bilmece.html", bilmece=secilen_bilmece)

if __name__ == "__main__":
    app.run(debug=True)
