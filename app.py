import os
from os.path import join, dirname
from dotenv import load_dotenv

from pymongo import MongoClient
import jwt
import hashlib
from flask import Flask, render_template, jsonify, request, session, redirect, url_for, make_response
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from fpdf import FPDF, XPos, YPos

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)
SECRET_KEY = "SPARTA"

# ================ surat ===============
def s_sktm(kepalaP, namaP, nikP, tempatP, tgl_lahirP, jkP, agamaP, pekerjaanP, alamatP, urusanP,code, no):
    terikini = datetime.now()
    tahun = terikini.strftime('%Y')
    bulan = terikini.strftime('%m')
    tanggal = terikini.strftime('%d')
    jam = terikini.strftime('%H.%M')
    if(bulan == '01'):
        bulan = "Januari"
        no_su = 'I'
    elif(bulan == '02'):
        bulan = "Februari"
        no_su = 'II'
    elif(bulan == '03'):
        bulan = "Maret"
        no_su = 'III'
    elif(bulan == '04'):
        bulan = "April"
        no_su = 'IV'
    elif(bulan == '05'):
        bulan = "Mei"
        no_su = 'V'
    elif(bulan == '06'):
        bulan = "Juni"
        no_su = 'VI'
    elif(bulan == '07'):
        bulan = "Juli"
        no_su = 'VII'
    elif(bulan == '08'):
        bulan = "Agustus"
        no_su = 'VIII'
    elif(bulan == '09'):
        bulan = "September"
        no_su = 'IX'
    elif(bulan == '10'):
        bulan = "Oktober"
        no_su = 'X'
    elif(bulan == '11'):
        bulan = "November"
        no_su = 'XI'
    elif(bulan == '12'):
        bulan = "Desember"
        no_su = 'XII'
    else :
        bulan = "Kiamat"

    class PDF(FPDF):
        def header(self):
            img_h = 42
            img_w = self.w-20
            x = (self.w - img_w) / 2
            y = 1
            self.image('static/img/header_limbungan.png', x, y, img_w, img_h)
            self.ln(45)
        
        def footer(self):
            self.set_y(-110)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145,10, f'Pekanbaru, {tanggal} {bulan} {tahun}', align='C')
            self.set_y(-104)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145.7999,10, "LURAH LIMBUNGAN", align='C')
            self.set_y(-70)
            self.set_font('helvetica', 'BU', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145.7999,10, "WELFINASARI HARAHAP, S.Sos", align='C')
            self.set_y(-65)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,10, " ", align='R')
            self.cell(145.7999,10, "NIP. 19840611 200801 2 007", align='C')

    def judulsurat(value):
        pdf.set_font('helvetica', 'BU', 12)
        pdf.cell(title_width,10, f'{value}', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def nomorsurat(value):
        pdf.set_font('helvetica', 'B', 12)
        pdf.cell(title_width,0, f'{value}', align='C')
        pdf.ln(15)
    def isi(content, value):
        pdf.cell(40,10, " ", align='R')
        pdf.cell(50,10, f'{content}',align='L')
        pdf.cell(10,10, ':',align='L')
        pdf.cell(85.7999,10, f'{value}',align='L')
        pdf.cell(30,10," ",align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT,)

    def paragraf(value):
        pdf.set_font('helvetica', '', 12)
        text = f'\t\t\t\t\t\t\t\t{value}'
        pdf.cell(30,10, " ", align='R')
        pdf.multi_cell(155.7999,10, text, align='J')
        pdf.cell(30,0," ",align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT,)

    pdf = PDF('P', 'mm', 'legal')
    # variable yang digunakan
    title_width = pdf.w - 2 * pdf.l_margin  # Lebar sel sejajar dengan lebar halaman

    judul = "SURAT KETERANGAN TIDAK MAMPU/MISKIN"
    nomor = no

    kepala = kepalaP
    nama = namaP
    NIK = nikP
    tempat = tempatP
    tgl_lahir = tgl_lahirP
    ttl = f'{tempat}, {tgl_lahir}'
    jk = jkP
    agama = agamaP
    status = "Menikah"
    pekerjaan = pekerjaanP
    alamat = alamatP
    urusan = urusanP

    pdf.add_page()

    judulsurat(judul)
    nomorsurat(f'No : {nomor}/LB/{no_su}/{tahun}')

    paragraf("Lurah Limbungan Kecamatan Rumbai Timur Kota Pekanbaru, dengan ini menerangkan bahwa :")

    isi("Nama", kepala)
    isi("NIK", NIK)
    isi("Tempat, Tanggal Lahir", ttl)
    isi("Jenis Kelamin", jk)
    isi("Agama", agama)
    isi("Status Perkawinan", status)
    isi("Pekerjaan", pekerjaan)
    isi("Alamat", alamat)

    paragraf(f'Benar nama tersebut diatas warga yang berdomisili di {alamat} Kelurahan Limbungan dan termasuk dalam {judul}')
    paragraf(f'Demikian keterangan ini dibuat dan dipergunakan untuk pengurusan {urusan} atas nama {nama}.')

    pdf.output(f'static/file/sktm-{code}-{nomor}.pdf')
def s_skdu(namaP, nikP, tempatP, ttlP, jkP, agamaP, statusP, pekerjaanP, alamatP, urusanP, nama_u, alamat_u, kelurahanU, kecamatanU, kotaU, code, nomor_surat,rt,rw):
    terikini = datetime.now()
    tahun = terikini.strftime('%Y')
    bulan = terikini.strftime('%m')
    tanggal = terikini.strftime('%d')
    if(bulan == '01'):
        bulan = "Januari"
        no_su = 'I'
    elif(bulan == '02'):
        bulan = "Februari"
        no_su = 'II'
    elif(bulan == '03'):
        bulan = "Maret"
        no_su = 'III'
    elif(bulan == '04'):
        bulan = "April"
        no_su = 'IV'
    elif(bulan == '05'):
        bulan = "Mei"
        no_su = 'V'
    elif(bulan == '06'):
        bulan = "Juni"
        no_su = 'VI'
    elif(bulan == '07'):
        bulan = "Juli"
        no_su = 'VII'
    elif(bulan == '08'):
        bulan = "Agustus"
        no_su = 'VIII'
    elif(bulan == '09'):
        bulan = "September"
        no_su = 'IX'
    elif(bulan == '10'):
        bulan = "Oktober"
        no_su = 'X'
    elif(bulan == '11'):
        bulan = "November"
        no_su = 'XI'
    elif(bulan == '12'):
        bulan = "Desember"
        no_su = 'XII'
    else :
        bulan = "Kiamat"

    class PDF(FPDF):
        def header(self):
            img_h = 42
            img_w = self.w-20
            x = (self.w - img_w) / 2
            y = 1
            self.image('static/img/header_limbungan.png', x, y, img_w, img_h)
            self.ln(45)
        def footer(self):
            self.set_y(-104)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145,10, f'Pekanbaru, {tanggal} {bulan} {tahun}', align='C')
            self.set_y(-100)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145.7999,10, "LURAH LIMBUNGAN", align='C')
            self.set_y(-70)
            self.set_font('helvetica', 'BU', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145.7999,10, "WELFINASARI HARAHAP, S.Sos", align='C')
            self.set_y(-65)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,10, " ", align='R')
            self.cell(145.7999,10, "NIP. 19840611 200801 2 007", align='C')
    def judulsurat(value):
        pdf.set_font('helvetica', 'BU', 12)
        pdf.cell(title_width,10, f'{value}', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    def nomorsurat(value):
        pdf.set_font('helvetica', 'B', 12)
        pdf.cell(title_width,0, f'{value}', align='C')
        pdf.ln(15)
    def isi(content, value):
        pdf.cell(40,6, " ", align='R')
        pdf.cell(50,6, f'{content}',align='L')
        pdf.cell(10,6, ':',align='L')
        pdf.cell(85.7999,6, f'{value}',align='L')
        pdf.cell(30,6," ",align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT,)
    def paragraf(value):
        pdf.set_font('helvetica', '', 12)
        text = f'{value}'
        pdf.cell(30,6, " ", align='R')
        pdf.multi_cell(155.7999,6, text, align='J')
        pdf.cell(30,0," ",align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT,)


    pdf = PDF('P', 'mm', 'legal')
    # variable yang digunakan
    title_width = pdf.w - 2 * pdf.l_margin  # Lebar sel sejajar dengan lebar halaman
    judul = "SURAT KETERANGAN DOMISILI USAHA"
    nomor = nomor_surat
    nama = namaP
    NIK = nikP
    tempat = tempatP
    tgl_lahir = ttlP
    ttl = f'{tempat}, {tgl_lahir}'
    jk = jkP
    agama = agamaP
    status = statusP
    pekerjaan = pekerjaanP
    alamat = alamatP
    urusan = urusanP

    pdf.add_page()
    judulsurat(judul)
    nomorsurat(f'No : {nomor}-SKDU/LB/{no_su}/{tahun}')
    paragraf("\t\t\t\t\t\t\t\tLurah Limbungan Kecamatan Rumbai Timur Kota Pekanbaru, dengan ini menerangkan bahwa :")
    isi("Nama", nama)
    isi("NIK", NIK)
    isi("Tempat, Tanggal Lahir", ttl)
    isi("Jenis Kelamin", jk)
    isi("Agama", agama)
    isi("Status Perkawinan", status)
    isi("Pekerjaan", pekerjaan)
    isi("Alamat", alamat)
    paragraf(f"\t\t\t\t\t\t\t\tBerdasarkan Surat Keterangan Nomor :{nomor}/SKDU-{no_su}/{tahun} yang diketahui oleh Ketua RT. {rt} RW. {rw}, benar yang bersangkutan diatas memiliki usaha :")
    jenis_usaha = nama_u
    alamat_usaha = alamat_u
    kelurahan = kelurahanU
    kecamatan = kecamatanU
    kota = kotaU
    isi("Jenis Usaha", jenis_usaha)
    isi("Alamat", alamat_usaha)
    isi("Kelurahan", kelurahan)
    isi("Kecamatan", kecamatan)
    isi("Kota", kota)
    paragraf(f'\t\t\t\t\t\t\t\tDengan persyaratan dan ketentuan-ketentuan sebagai berikut :')
    paragraf(f"\t\t\t\t\t\t\t\t1.\tTidak melakukan penyalahgunaan tempat usaha;")
    paragraf(f"\t\t\t\t\t\t\t\t2.\tUntuk Memenuhi segala peraturan, hukum dan norma yang berlaku di \t\t\t\t\t\t\t\t\t\t\t\twilayah Kelurahan Limbungan Kecamatan Rumbai Timur Kota \t\t\t\t\t\t\t\t\t\t\t\tPekanbaru;")
    paragraf(f"\t\t\t\t\t\t\t\t3.\tUntuk selalu menjaga kebersihan, keindahan, ketertiban dan keamanan \t\t\t\t\t\t\t\t\t\t\t\tdiwilayah /lingkungan tempat usaha yang bersangkutan;")
    paragraf(f"\t\t\t\t\t\t\t\t4.\tMemenuhi segala kewajiban dan retribusi yang diatur sesuai dengan \t\t\t\t\t\t\t\t\t\t\t\tundang-undang yang berlaku.")
    paragraf(f'\t\t\t\t\t\t\t\tDemikian surat keterangan ini kami buat dengan sebenarnya dan dipergunakan untuk {urusan}.')
    pdf.output(f'static/file/skdu-{code}-{nomor}.pdf')
def s_skk(nama_k, nik_k, ttl_k, jk_k, alamat_k, agama_k, status_k, pekerjaan_k, kewarganegaraan_k, hari_k, tgl_k, pukul_k, tempat_k, penyebab_k, nama_pem, tmpt_pem, tgl_pem, nik_pem, jk_pem, alamat_pem, hubungan_pem, code, no):
    terikini = datetime.now()
    tahun = terikini.strftime('%Y')
    bulan = terikini.strftime('%m')
    tanggal = terikini.strftime('%d')
    jam = terikini.strftime('%H.%M')
    if(bulan == '01'):
        bulan = "Januari"
        no_su = 'I'
    elif(bulan == '02'):
        bulan = "Februari"
        no_su = 'II'
    elif(bulan == '03'):
        bulan = "Maret"
        no_su = 'III'
    elif(bulan == '04'):
        bulan = "April"
        no_su = 'IV'
    elif(bulan == '05'):
        bulan = "Mei"
        no_su = 'V'
    elif(bulan == '06'):
        bulan = "Juni"
        no_su = 'VI'
    elif(bulan == '07'):
        bulan = "Juli"
        no_su = 'VII'
    elif(bulan == '08'):
        bulan = "Agustus"
        no_su = 'VIII'
    elif(bulan == '09'):
        bulan = "September"
        no_su = 'IX'
    elif(bulan == '10'):
        bulan = "Oktober"
        no_su = 'X'
    elif(bulan == '11'):
        bulan = "November"
        no_su = 'XI'
    elif(bulan == '12'):
        bulan = "Desember"
        no_su = 'XII'
    else :
        bulan = "Kiamat"

    class PDF(FPDF):
        def header(self):
            img_h = 42
            img_w = self.w-20
            x = (self.w - img_w) / 2
            y = 1
            self.image('static/img/header_limbungan.png', x, y, img_w, img_h)
            self.ln(45)
        def footer(self):
            self.set_y(-94)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145,10, f'Pekanbaru, {tanggal} {bulan} {tahun}', align='C')
            self.set_y(-90)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145.7999,10, "LURAH LIMBUNGAN", align='C')
            self.set_y(-60)
            self.set_font('helvetica', 'BU', 12)
            self.cell(70,5, " ", align='R')
            self.cell(145.7999,10, "WELFINASARI HARAHAP, S.Sos", align='C')
            self.set_y(-55)
            self.set_font('helvetica', 'B', 12)
            self.cell(70,10, " ", align='R')
            self.cell(145.7999,10, "NIP. 19840611 200801 2 007", align='C')
    def judulsurat(value):
        pdf.set_font('helvetica', 'BU', 12)
        pdf.cell(title_width,10, f'{value}', new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    def nomorsurat(value):
        pdf.set_font('helvetica', 'B', 12)
        pdf.cell(title_width,0, f'{value}', align='C')
        pdf.ln(15)
    def isi(content, value):
        pdf.cell(40,6, " ", align='R')
        pdf.cell(50,6, f'{content}',align='L')
        pdf.cell(10,6, ':',align='L')
        pdf.cell(85.7999,6, f'{value}',align='L')
        pdf.cell(30,6," ",align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT,)
    def paragraf(value):
        pdf.set_font('helvetica', '', 12)
        text = f'{value}'
        pdf.cell(30,6, " ", align='R')
        pdf.multi_cell(155.7999,6, text, align='J')
        pdf.cell(30,0," ",align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf = PDF('P', 'mm', 'legal')
    # variable yang digunakan
    title_width = pdf.w - 2 * pdf.l_margin  # Lebar sel sejajar dengan lebar halaman
    judul = "SURAT KETERANGAN KEMATIAN"
    nomor = no
    # DATA YANG MENINGGAL
    nama = nama_k
    NIK = nik_k
    ttl = ttl_k
    jk = jk_k
    alamat = alamat_k
    agama = agama_k
    status = status_k
    pekerjaan = pekerjaan_k
    kewarganegaraan = kewarganegaraan_k

    pdf.add_page()
    judulsurat(judul)
    nomorsurat(f'No : {nomor}-SKK/LB/{no_su}/{tahun}')
    paragraf("\t\t\t\t\t\t\t\tLurah Limbungan Kecamatan Rumbai Timur Kota Pekanbaru, dengan ini menerangkan bahwa :")
    # DATA YANG MENINGGAL
    isi("Nama", nama)
    isi("NIK", NIK)
    isi("Tempat, Tanggal Lahir", ttl)
    isi("Jenis Kelamin", jk)
    isi("Alamat", alamat)
    isi("Agama", agama)
    isi("Status Perkawinan", status)
    isi("Pekerjaan Terakhir", pekerjaan)
    isi("Kewarganegaraan", kewarganegaraan)
    paragraf(f"\t\t\t\t\t\t\t\tBerdasarkan Surat Keterangan Kematian No : {nomor}/SKK/{no_su}/2023, bahwa Orang tersebut diatas benar telah Meninggal Dunia pada :")

    # KETERANGAN YANG MENINGGAL
    hari = hari_k
    hari_tgl = tgl_k
    pukul = f'{pukul_k} WIB'
    tempat = tempat_k
    penyebab = penyebab_k

    # KETERANGAN YANG MENINGGAL
    isi("Hari", hari)
    isi("Tanggal", hari_tgl)
    isi("Pukul", pukul)
    isi("Bertempat di", tempat)
    isi("Penyebab Kematian", penyebab)
    pdf.cell(215,5, " ",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    paragraf(f'\t\t\t\t\t\t\t\tSurat Keterangan ini dibuat berdasarkan laporan dari :')
    # DATA PELAPOR
    nama_p = nama_pem
    tmpt_p = tmpt_pem
    tgl_p = tgl_pem
    ttl_p = f"{tmpt_p}, {tgl_p}"
    nik_p = nik_pem
    jk_p = jk_pem
    alamat_p = alamat_pem
    hubungan_p = hubungan_pem

    # DATA PELAPOR
    isi("Nama", nama_p)
    isi("Tempat/Tgl.Lahir", ttl_p)
    isi("NIK", nik_p)
    isi("Jenis Kelamin", jk_p)
    isi("Alamat", alamat_p)
    isi("Hubungan", hubungan_p)
    pdf.cell(215,5, " ",new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    paragraf(f'\t\t\t\t\t\t\t\tDemikian Surat Keterangan ini kami buat, untuk dipergunakan sebagaimana mestinya.')


    pdf.output(f'static/file/skk-{code}-{nomor}.pdf')

# ================= route ==============
@app.route('/')
def home():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.akun.find_one({"username": payload["id"]})
        if(user_info['role'] == "rw"):
            rw = user_info['code']
            rw = str(rw)
            total_diterima = db.pengurusan.count_documents({"status-rw": "diterima", "rw":rw})
            total_belum_diterima = db.pengurusan.count_documents({"status-rw": "belum diterima", "rw" : rw})
            total_diterima = int(total_diterima)
            total_belum_diterima = int(total_belum_diterima)
            return render_template("index.html", userinfo=user_info, status_1=total_diterima,status_0=total_belum_diterima)
        elif(user_info['role'] == "rt"):
            return render_template("index.html", userinfo=user_info)
        elif(user_info['role'] == "lurah"):
            tot_rt = user_info['jumlah_rt']
            tot_rt = int(tot_rt)
            tot_rw = user_info['jumlah_rw']
            tot_rw = int(tot_rw)
            total_belum_diterima = db.pengurusan.count_documents({"status-rw": "belum diterima"})
            total_belum_diterima = int(total_belum_diterima)
            total_diterima = db.pengurusan.count_documents({"status-rw": "diterima"})
            total_diterima = int(total_diterima)
            return render_template("index.html", userinfo=user_info,totrt=tot_rt, totrw=tot_rw, status_0=total_belum_diterima, status_1=total_diterima)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))

@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template(
        'login.html', msg=msg
    )

@app.route('/daftar', methods=['GET'])
def daftar():
    msg = request.args.get("msg")
    return render_template(
        'daftar.html', msg=msg
    )

@app.route('/buat-surat', methods=["GET"])
def suket():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.akun.find_one({"username": payload["id"]})
        return render_template("suket.html", userinfo=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))

@app.route('/informasi/pengurusan', methods=["GET"])
def pengurusan():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.akun.find_one({"username": payload["id"]})
        if(user_info['role'] == "rw"):
            rw = user_info['code']
            rw = str(rw)
            total_diterima = db.pengurusan.count_documents({"status-rw": "diterima", "rw":rw})
            total_belum_diterima = db.pengurusan.count_documents({"status-rw": "belum diterima", "rw" : rw})
            total_diterima = int(total_diterima)
            total_belum_diterima = int(total_belum_diterima)
            return render_template("list-pengurusan.html", userinfo=user_info, status_1=total_diterima,status_0=total_belum_diterima)
        elif(user_info['role'] == "rt"):
            return render_template("list-pengurusan.html", userinfo=user_info)
        elif(user_info['role'] == "lurah"):
            total_diterima = db.pengurusan.count_documents({"status-rw": "diterima"})
            total_belum_diterima = db.pengurusan.count_documents({"status-rw": "belum diterima"})
            total_diterima = int(total_diterima)
            total_belum_diterima = int(total_belum_diterima)
            return render_template("list-pengurusan.html", userinfo=user_info, status_1=total_diterima,status_0=total_belum_diterima)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))

@app.route('/informasi/pengurusan/diizinkan', methods=["GET"])
def diiznkan():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.akun.find_one({"username": payload["id"]})
        if(user_info['role'] == "rw"):
            rw = user_info['code']
            rw = str(rw)
            total_diterima = db.pengurusan.count_documents({"status-rw": "diterima", "rw":rw})
            total_belum_diterima = db.pengurusan.count_documents({"status-rw": "belum diterima", "rw" : rw})
            total_diterima = int(total_diterima)
            total_belum_diterima = int(total_belum_diterima)
            return render_template("list-diizinkan.html", userinfo=user_info, status_1=total_diterima,status_0=total_belum_diterima)
        elif(user_info['role'] == "rt"):
            return render_template("list-diizinkan.html", userinfo=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))

@app.route('/informasi/pengurusan/belum-diizinkan', methods=["GET"])
def blm_diizinkan():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.akun.find_one({"username": payload["id"]})
        if(user_info['role'] == "rw"):
            rw = user_info['code']
            rw = str(rw)
            total_diterima = db.pengurusan.count_documents({"status-rw": "diterima", "rw":rw})
            total_belum_diterima = db.pengurusan.count_documents({"status-rw": "belum diterima", "rw" : rw})
            total_diterima = int(total_diterima)
            total_belum_diterima = int(total_belum_diterima)
            return render_template("list-blmdiizinkan.html", userinfo=user_info, status_1=total_diterima,status_0=total_belum_diterima)
        elif(user_info['role'] == "rt"):
            return render_template("list-blmdiizinkan.html", userinfo=user_info)
        elif(user_info['role'] == "lurah"):
            total_belum_diterima = db.pengurusan.count_documents({"status-rw": "belum diterima"})
            total_belum_diterima = int(total_belum_diterima)
            total_diterima = db.pengurusan.count_documents({"status-rw": "diterima"})
            total_diterima = int(total_diterima)
            return render_template("list-blmdiizinkan.html", userinfo=user_info,status_0=total_belum_diterima, status_1=total_diterima)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))

@app.route('/surat/<keyword>', methods=["GET"])
def surat(keyword):
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.akun.find_one({"username": payload["id"]})
        x = keyword
        total_belum_diterima = db.pengurusan.count_documents({"status-rw": "belum diterima"})
        total_belum_diterima = int(total_belum_diterima)
        total_diterima = db.pengurusan.count_documents({"status-rw": "diterima"})
        total_diterima = int(total_diterima)
        return render_template("surat-surat.html", userinfo=user_info, rw = x,status_0=total_belum_diterima, status_1=total_diterima)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))

# =============== support system ===============
@app.route("/sign_in", methods=["POST"])
def sign_in():
    # Sign in
    username_receive = request.form["username_give"]
    password_receive = request.form["password_give"]
    pw_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()
    print(username_receive, pw_hash)
    result = db.akun.find_one(
        {
            "username": username_receive,
            "password": pw_hash,
        }
    )
    if result:
        payload = {
            "id": username_receive,
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256").decode("utf-8")
        return jsonify(
            {
                "result": "success",
                "token": token,
            }
        )
    else:
        return jsonify(
            {
                "result": "fail",
                "msg": "We could not find a user with that id/password combination",
            }
        )
@app.route("/api/login", methods=["POST"])
def api_login():
    id_receive = request.form["id_give"]
    pw_receive = request.form["pw_give"]
    pw_hash = hashlib.sha256(pw_receive.encode("utf-8")).hexdigest()
    result = db.akun.find_one({"id": id_receive, "pw": pw_hash})
    if result is not None:
        payload = {
            "id": id_receive,
            "exp": datetime.utcnow() + timedelta(seconds = 60 * 60 * 24),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256").decode("utf-8")
        return jsonify({"result": "success", "token": token})
    else:
        return jsonify(
            {"result": "fail", "msg": "Either your email or your password is incorrect"}
        )
@app.route("/api/nick", methods=["GET"])
def api_valid():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        userinfo = db.akun.find_one({"id": payload["id"]}, {"_id": 0})
        return jsonify({"result": "success", "nickname": userinfo["nick"]})
    except jwt.ExpiredSignatureError:
        return jsonify({"result": "fail", "msg": "Your token has expired"})
    except jwt.exceptions.DecodeError:
        return jsonify(
            {"result": "fail", "msg": "There was an error while logging you in"}
        )
@app.route('/logout', methods=['GET'])
def logout():
    response = make_response(redirect('/login?msg=There+was+problem+logging+you+in'))
    response.set_cookie('mytoken', '', expires=0)
    return response
@app.route('/sign_up', methods=["POST"])
def sign_up():
    username_receive = request.form['username_give']
    code_receive = request.form['code_give']
    nick_receive = request.form['nick_give']
    rt_receive = request.form['rt_give']
    role_receive = "rt"
    password_receive = request.form['password_give']
    pw_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()
    doc = {
        "username" : username_receive,
        "password" : pw_hash,
        "code" : code_receive,
        "nick" : nick_receive,
        "rt" : rt_receive,
        "role" : role_receive,
    }
    db.akun.insert_one(doc)
    return jsonify({
        'msg': "Berhasil Tersimpan"
    })
@app.route('/data', methods=["POST"])
def kirim_data() :
    nama_receive = request.form['nama_give']
    agama_receive = request.form['agama_give']
    nik_receive = request.form['nik_give']
    ttl_receive = request.form['ttl_give']
    status_receive = request.form['status_give']
    alamat_receive = request.form['alamat_give']
    pekerjaan_receive = request.form['pekerjaan_give']
    jk_receive = request.form['jk_give']
    pengajuan_receive = request.form['pengajuan_give']
    nomorHP_receive = request.form['nomorHP_give']
        
    get = db.warga.find_one({"nik" : nik_receive})
    getKepala = get['kepala']
    getRT = get['rt']
    getRW = get['rw']
    get = db.kartu_keluarga.find_one({"kepala" : getKepala})
    getKK = get['gambar']
    gambar = getKK.split("/")[-1]

    x = datetime.now()
    tanggal = x.strftime('%Y-%m-%d')
    waktu = x.strftime('%H:%M:%S')

    total = db.pengurusan.count_documents({})
    total = int(total)
    total = total + 1

    if(pengajuan_receive == "Surat Keterangan Tidak Mampu") :
        getWarga = db.warga.find_one({"nama" : getKepala})
        keterangan_receive = request.form['keterangan_give']
        agama = getWarga['agama']
        nik = getWarga['nik']
        pekerjaan = getWarga['pekerjaan']
        jk = getWarga['jk']
        rt = getWarga['rt']
        rw = getWarga['rw']
        ttl = getWarga['tgl_lahir']
        doc = {
            "nama" : nama_receive,
            "kepala" : getKepala,
            "nik" : nik_receive,
            "tgl_lahir" : ttl_receive,
            "alamat" : alamat_receive,
            "jk" : jk_receive,
            "agama" : agama_receive,
            "status" : status_receive,
            "pekerjaan" : pekerjaan_receive,
            "kontak" : nomorHP_receive,
            "gambar" : gambar,
            "code" : total,
            "rt" : getRT,
            "rw" : getRW,
            "jenis_surat" : pengajuan_receive,
            "tanggal_pengajuan" : tanggal,
            "waktu_pengajuan" : waktu,
            "status-rt" : "diterima",
            "status-rw" : "belum diterima",
        }
        doc_surat = {
            "code" : total,
            "kepala" : getKepala,
            "nik" : nik,
            "ttl" : ttl,
            "jk" : jk,
            "agama" : agama,
            "status" : "Menikah",
            "pekerjaan" : pekerjaan,
            "alamat" : alamat_receive,
            "keterangan" : keterangan_receive,
            "nama_pemohon" : nama_receive,
            "rt" : rt,
            "rw" : rw,
            "nomor_surat" : 000,
        }
        db.sktm.insert_one(doc_surat)
    elif(pengajuan_receive == "Surat Keterangan Usaha") :
        namaU_receive = request.form['namaU_give'],
        alamatU_receive = request.form['alamatU_give'],
        urusanU_receive = request.form['urusanU_give'],
        doc = {
            "nama" : nama_receive,
            "kepala" : getKepala,
            "nik" : nik_receive,
            "tgl_lahir" : ttl_receive,
            "alamat" : alamat_receive,
            "jk" : jk_receive,
            "agama" : agama_receive,
            "status" : status_receive,
            "pekerjaan" : pekerjaan_receive,
            "kontak" : nomorHP_receive,
            "gambar" : gambar,
            "code" : total,
            "rt" : getRT,
            "rw" : getRW,
            "jenis_surat" : pengajuan_receive,
            "tanggal_pengajuan" : tanggal,
            "waktu_pengajuan" : waktu,
            "status-rt" : "diterima",
            "status-rw" : "belum diterima",
        }
        doc_surat = {
            "code" : total,
            "kepala" : getKepala,
            "nik" : nik_receive,
            "ttl" : ttl_receive,
            "jk" : jk_receive,
            "agama" : agama_receive,
            "status" : status_receive,
            "pekerjaan" : pekerjaan_receive,
            "alamat" : alamat_receive,
            "nama_pemohon" : nama_receive,
            "nama_usaha" : namaU_receive,
            "alamat_usaha" : alamatU_receive,
            "urusan_usaha" : urusanU_receive,
            "kelurahan" : "Limbungan",
            "kecamatan" : "Rumbai Timur",
            "kota" : "Pekanbaru",
            "rt" : getRT,
            "rw" : getRW,
            "nomor_surat" : 251,
        }
        db.skdu.insert_one(doc_surat)
    elif(pengajuan_receive == "Surat Keterangan Kematian") :
        hubungan_k = request.form['hubungan_k'],
        nama_k = request.form['nama_k'],
        nik_k = request.form['nik_k'],
        ttl_k = request.form['ttl_k'],
        agama_k = request.form['agama_k'],
        jk_k = request.form['jk_k'],
        status_k = request.form['status_k'],
        pekerjaan_k = request.form['pekerjaan_k'],
        kewarganegaraan_k = request.form['kewarganegaraan_k'],
        alamat_k = request.form['alamat_k'],
        hari_k = request.form['hari_k'],
        tanggal_k = request.form['tanggal_k'],
        pukul_k = request.form['pukul_k'],
        bertempat_k = request.form['bertempat_k'],
        penyebab_k = request.form['penyebab_k'],
        doc = {
            "nama" : nama_receive,
            "kepala" : getKepala,
            "nik" : nik_receive,
            "tgl_lahir" : ttl_receive,
            "alamat" : alamat_receive,
            "jk" : jk_receive,
            "agama" : agama_receive,
            "status" : status_receive,
            "pekerjaan" : pekerjaan_receive,
            "kontak" : nomorHP_receive,
            "gambar" : gambar,
            "code" : total,
            "rt" : getRT,
            "rw" : getRW,
            "jenis_surat" : pengajuan_receive,
            "tanggal_pengajuan" : tanggal,
            "waktu_pengajuan" : waktu,
            "status-rt" : "diterima",
            "status-rw" : "belum diterima",
        }
        x = db.warga.find_one({'nik' : nik_receive})
        tmpt_lahir = x['tmpt_lahir']
        doc_surat = {
            "code" : total,
            "nama_k" : nama_k,
            "nik_k" : nik_k,
            "ttl_k" : ttl_k,
            "jk_k" : jk_k,
            "agama_k" : agama_k,
            "status_k" : status_k,
            "pekerjaan_k" : pekerjaan_k,
            "kewarganegaraan_k" : kewarganegaraan_k,
            "alamat_k" : alamat_k,
            "hari_k" : hari_k,
            "tanggal_k" : tanggal_k,
            "pukul_k" : pukul_k,
            "bertempat_k" : bertempat_k,
            "penyebab_k" : penyebab_k,
            "nama_pemohon" : nama_receive,
            "tmpt_lahir_pemohon" : tmpt_lahir,
            "tgl_lahir_pemohon" : ttl_receive,
            "nik_pemohon" : nik_receive,
            "jk_pemohon" : jk_receive,
            "alamat_pemohon" : alamat_receive,
            "hubungan_pemohon" : hubungan_k,
            "rt" : getRT,
            "rw" : getRW,
            "nomor_surat" : 000,
        }
        db.skk.insert_one(doc_surat)

    db.pengurusan.insert_one(doc)
    return jsonify({
        'msg' : 'Surat Berhasil Dibuat, Silahkan Hubungi Ketua RW '+getRW+' !',
        'header' : 'Berhasil'
    })

@app.route('/perizinan', methods=['POST'])
def perizinan() :
    status_receive = request.form['status_give']
    code_receive = request.form['code_give']
    code_receive = int(code_receive)

    data = db.pengurusan.find_one({'code' : code_receive})
    jenis = data['jenis_surat']
    rt = data['rt']
    rw = data['rw']
    if jenis == "Surat Keterangan Tidak Mampu" :
        sktm = db.sktm.find_one({'code' : code_receive})
        kepala = sktm['kepala']
        nama = sktm['nama_pemohon']
        nik = sktm['nik']
        sktm_p = db.warga.find_one({'nik' : nik})
        tempat = sktm_p['tmpt_lahir']
        tgl_l = sktm['ttl']
        jk = sktm['jk']
        agama = sktm['agama']
        pekerjaan = sktm['pekerjaan']
        alamat = sktm['alamat']
        urusan = sktm['keterangan']
        latest_documents = db.sktm.find({}, {'_id': 0, 'nomor_surat': 1}).sort('nomor_surat', -1).limit(2)
        latest_ids = []
        for document in latest_documents:
            latest_ids.append(document['nomor_surat'])
        previous_code = latest_ids[0] if len(latest_ids) >= 2 else None
        previous_code = previous_code
        no_su = previous_code+1
        db.sktm.update_one(
            {'code' : code_receive},
            {'$set' : {'nomor_surat' : no_su}}
        )
        s_sktm(kepala, nama, nik, tempat, tgl_l, jk, agama, pekerjaan, alamat, urusan, code_receive, no_su)
        doc = {
            "status-rw" : status_receive,
            "file" : f'sktm-{code_receive}-{no_su}.pdf'
        }
    elif jenis == "Surat Keterangan Usaha" :
        skdu = db.skdu.find_one({'code' : code_receive})
        nama = skdu['nama_pemohon']
        nik = skdu['nik']
        skdu_p = db.warga.find_one({'nik' : nik})
        tempat = skdu_p['tmpt_lahir']
        ttl = skdu['ttl']
        jk = skdu['jk']
        agama = skdu['agama']
        status = skdu['status']
        pekerjaan = skdu['pekerjaan']
        alamat = skdu['alamat']
        urusan_usaha = skdu['urusan_usaha'][0]
        nama_usaha = skdu['nama_usaha'][0]
        alamat_usaha = skdu['alamat_usaha'][0]
        kelurahan_usaha = skdu['kelurahan']
        kecamatan_usaha = skdu['kecamatan']
        kota_usaha = skdu['kota']
        
        latest_documents = db.skdu.find({}, {'_id': 0, 'nomor_surat': 1}).sort('nomor_surat', -1).limit(2)
        latest_ids = []
        for document in latest_documents:
            latest_ids.append(document['nomor_surat'])
        previous_code = latest_ids[0] if len(latest_ids) >= 2 else None
        no_su = previous_code+1
        db.skdu.update_one(
            {'code' : code_receive},
            {'$set' : {'nomor_surat' : no_su}}
        )
        s_skdu(nama, nik, tempat, ttl, jk, agama, status, pekerjaan, alamat, urusan_usaha,nama_usaha, alamat_usaha, kelurahan_usaha, kecamatan_usaha, kota_usaha, code_receive, no_su, rt, rw)
        doc = {
            "status-rw" : status_receive,
            "file" : f'skdu-{code_receive}-{no_su}.pdf'
        }
    elif jenis == "Surat Keterangan Kematian" :
        skk = db.skk.find_one({'code' : code_receive})
        nama_k = skk['nama_k'][0]
        nik_k = skk['nik_k'][0]
        ttl_k = skk['ttl_k'][0]
        jk_k = skk['jk_k'][0]
        agama_k = skk['agama_k'][0]
        status_k = skk['status_k'][0]
        pekerjaan_k = skk['pekerjaan_k'][0]
        alamat_k = skk['alamat_k'][0]
        kewarganegaraan_k = skk['kewarganegaraan_k'][0]
        hari_k = skk['hari_k'][0]
        tanggal_k = skk['tanggal_k'][0]
        pukul_k = skk['pukul_k'][0]
        bertempat_k = skk['bertempat_k'][0]
        penyebab_k = skk['penyebab_k'][0]
        nama_pemohon = skk['nama_pemohon']
        nik_pemohon = skk['nik_pemohon']
        tmpt_lahir_pemohon = skk['tmpt_lahir_pemohon']
        tgl_lahir_pemohon = skk['tgl_lahir_pemohon']
        jk_pemohon = skk['jk_pemohon']
        alamat_pemohon = skk['alamat_pemohon']
        hubungan_pemohon = skk['hubungan_pemohon'][0]
        latest_documents = db.skk.find({}, {'_id': 0, 'nomor_surat': 1}).sort('nomor_surat', -1).limit(2)
        latest_ids = []
        for document in latest_documents:
            latest_ids.append(document['nomor_surat'])
        previous_code = latest_ids[0] if len(latest_ids) >= 2 else None
        no_su = previous_code+1
        db.skk.update_one(
            {'code' : code_receive},
            {'$set' : {'nomor_surat' : no_su}}
        )
        s_skk(nama_k, nik_k,ttl_k, jk_k, alamat_k, agama_k, status_k, pekerjaan_k, kewarganegaraan_k, hari_k, tanggal_k, pukul_k, bertempat_k, penyebab_k, nama_pemohon, tmpt_lahir_pemohon, tgl_lahir_pemohon, nik_pemohon, jk_pemohon, alamat_pemohon, hubungan_pemohon, code_receive, no_su)
        doc = {
            "status-rw" : status_receive,
            "file" : f'skk-{code_receive}-{no_su}.pdf'
        }
    db.pengurusan.update_one(
        {'code' : code_receive},
        {'$set' : doc})
    return jsonify({
        'msg' : 'Surat Telah Diizinkan !',
        'header' : 'Berhasil'})
# ================= API ==================
@app.route("/warga", methods=["GET"])
def warga_get():
    
    token_receive = request.cookies.get("mytoken")
    try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.akun.find_one({"username": payload["id"]})
            warga_list = list(db.warga.find({}, {'_id': False}))

            if user_info['role'] == "rt":
                rt =user_info['rt']
                rw =user_info['code']
                return jsonify({'warga': warga_list, "rt":rt, "rw":rw})
            elif user_info['role'] == "rw" :
                rt = "" 
                rw =user_info['code']
                return jsonify({'warga': warga_list, "rt":rt, "rw":rw})
            elif user_info['role'] == "lurah" :
                x = user_info['role']
                return jsonify({'warga': warga_list, "lurah" : x})
            
    except jwt.ExpiredSignatureError:
            return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
            return redirect(url_for("login", msg="There was problem logging you in"))
    
@app.route("/pengurusan", methods=["GET"])
def pengurusan_get():
    token_receive = request.cookies.get("mytoken")
    try:
            payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
            user_info = db.akun.find_one({"username": payload["id"]})
            pengurusan_list = list(db.pengurusan.find({}, {'_id': False}))
            if(user_info['role'] == "rt"):
                rt =user_info['rt'] 
                rw =user_info['code']
                return jsonify({'pengurusan': pengurusan_list, "rt":rt, "rw":rw})
            elif(user_info['role'] == "rw"):
                rt = ""
                rw =user_info['code']
                return jsonify({'pengurusan': pengurusan_list, "rt":rt, "rw":rw})
            elif(user_info['role'] == 'lurah') :
                lurah = "lurah"
                return jsonify({'pengurusan': pengurusan_list,  "lurah":lurah})
    except jwt.ExpiredSignatureError:
            return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
            return redirect(url_for("login", msg="There was problem logging you in"))


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)