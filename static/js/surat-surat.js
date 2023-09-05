$(document).ready(function () {
    $('#surat').empty()
    $.ajax({
        type: "GET",
        url: "/pengurusan",
        data: {},
        success: function (response) {
            data = response['pengurusan']
            no = 1
            for (let i = 0; i < data.length; i++) {
                rw = data[i]['rw']
                jenis = data[i]['jenis_surat']
                rt = data[i]['rt']
                code = data[i]['code']
                status_rw = data[i]['status-rw']
                var lastUrl = window.location.href;
                lastUrl = lastUrl.split("/")
                if (rw == lastUrl[4] && status_rw == "diterima") {
                    nama = data[i]['nama']
                    tanggal = data[i]['tanggal_pengajuan']
                    waktu = data[i]['waktu_pengajuan']
                    status_rw = data[i]['status-rw']
                    kepala = data[i]['kepala']
                    nik = data[i]['nik']
                    agama = data[i]['agama']
                    alamat = data[i]['alamat']
                    gambar = data[i]['gambar']
                    kontak = data[i]['kontak']
                    file = data[i]['file']
                    jk = data[i]['jk']
                    if (status_rw == "diterima") {
                        rwCLass = "rw"
                    } else {
                        rwCLass = "rw-lock"
                    }
                    let html =
                        `
                    <tr>
                        <th scope="row">${no}</th>
                        <td>${jenis}</td>
                        <td><a href="/" type="button" data-bs-toggle="modal" data-bs-target="#info${code}"> ${nama}</a></td>
                        
                        <td>${tanggal}<br><p>${waktu}</p></td>
                        <td><p class="rt">${rt}</p></td>
                        <td><p class="${rwCLass}">${rw}</p></td>
                        <td><a class="btn izinkan-button" style="color: blue;" href="microsoft-edge:http://127.0.0.1:8000/static/file/${file}">Unduh</a></td>
                    </tr>
                    `
                    let html2 =
                        `
                    <div class="modal fade" id="info${code}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h1 class="modal-title fs-5" id="exampleModalLabel">Pengurusan ${jenis}</h1>
                                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                </div>
                                <div class="modal-body row">
                                    <div class="col-6 mb-3">
                                        <p>Nama Pemohon : </p><p>${nama}</p>
                                    </div>
                                    <div class="col-6 mb-3">
                                        <p>Kepala Keluarga : </p><p>${kepala}</p>
                                    </div>
                                    <div class="col-6 mb-3">
                                        <p>NIK Pemohon : </p><p>${nik}</p>
                                    </div>
                                    <div class="col-6 mb-3">
                                        <p>Agama : </p><p>${agama}</p>
                                    </div>
                                    <div class="col-6 mb-3">
                                        <p>Jenis Kelamin : </p><p>${jk}</p>
                                    </div>
                                    <div class="col-6 mb-3">
                                        <p>Alamat : </p><p>${alamat}</p>
                                    </div>
                                    <div class="mb-3">
                                        <p>Kontak : </p><a href="https://wa.me/${kontak}">${kontak} (Click to check Whatsapp)</a>
                                    </div>
                                    <div class="mb-3">
                                        <p>Gambar Kartu Keluarga : </p><img src="../static/img/${gambar}" class="img-fluid d-block">
                                    </div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal">OK</button>
                                </div>
                            </div>
                        </div>
                    </div>
                    `
                    $('#surat').prepend(html)
                    $('#simpan-modal').prepend(html2)
                    no = no + 1
                }
            }
        }
    })
})

$("#pengajuan").change(function () {
    var surat = $(this).val();
    $('#surat').empty()
    $.ajax({
        type: "GET",
        url: "/pengurusan",
        data: {},
        success: function (response) {
            data = response['pengurusan']
            no = 1
            for (let i = 0; i < data.length; i++) {
                jenis = data[i]['jenis_surat']
                if (surat == "all") {
                    rw = data[i]['rw']
                    jenis = data[i]['jenis_surat']
                    rt = data[i]['rt']
                    code = data[i]['code']
                    status_rw = data[i]['status-rw']
                    var lastUrl = window.location.href;
                    lastUrl = lastUrl.split("/")
                    if (rw == lastUrl[4] && status_rw == "diterima") {
                        nama = data[i]['nama']
                        tanggal = data[i]['tanggal_pengajuan']
                        waktu = data[i]['waktu_pengajuan']
                        status_rw = data[i]['status-rw']
                        kepala = data[i]['kepala']
                        nik = data[i]['nik']
                        agama = data[i]['agama']
                        alamat = data[i]['alamat']
                        gambar = data[i]['gambar']
                        kontak = data[i]['kontak']
                        jk = data[i]['jk']
                        if (status_rw == "diterima") {
                            rwCLass = "rw"
                        } else {
                            rwCLass = "rw-lock"
                        }
                        let html =
                            `
                        <tr>
                            <th scope="row">${no}</th>
                            <td>${jenis}</td>
                            <td><a href="/" type="button" data-bs-toggle="modal" data-bs-target="#info${code}"> ${nama}</a></td>
                            
                            <td>${tanggal}<br><p>${waktu}</p></td>
                            <td><p class="rt">${rt}</p></td>
                            <td><p class="${rwCLass}">${rw}</p></td>
                            <td><a class="btn izinkan-button" style="color: blue;" href="microsoft-edge:http://127.0.0.1:8000/static/file/${file}">Unduh</a></td>
                        </tr>
                        `
                        let html2 =
                            `
                        <div class="modal fade" id="info${code}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="exampleModalLabel">Pengurusan ${jenis}</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body row">
                                        <div class="col-6 mb-3">
                                            <p>Nama Pemohon : </p><p>${nama}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Kepala Keluarga : </p><p>${kepala}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>NIK Pemohon : </p><p>${nik}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Agama : </p><p>${agama}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Jenis Kelamin : </p><p>${jk}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Alamat : </p><p>${alamat}</p>
                                        </div>
                                        <div class="mb-3">
                                            <p>Kontak : </p><a href="https://wa.me/${kontak}">${kontak} (Click to check Whatsapp)</a>
                                        </div>
                                        <div class="mb-3">
                                            <p>Gambar Kartu Keluarga : </p><img src="../static/img/${gambar}" class="img-fluid d-block">
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">OK</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        `
                        $('#surat').prepend(html)
                        $('#simpan-modal').prepend(html2)
                        no = no + 1
                    }
                } else if (surat == "Surat Keterangan Usaha") {
                    rw = data[i]['rw']
                    jenis = data[i]['jenis_surat']
                    rt = data[i]['rt']
                    code = data[i]['code']
                    status_rw = data[i]['status-rw']
                    var lastUrl = window.location.href;
                    lastUrl = lastUrl.split("/")
                    if (rw == lastUrl[4] && status_rw == "diterima" && jenis == surat) {
                        nama = data[i]['nama']
                        tanggal = data[i]['tanggal_pengajuan']
                        waktu = data[i]['waktu_pengajuan']
                        status_rw = data[i]['status-rw']
                        kepala = data[i]['kepala']
                        nik = data[i]['nik']
                        agama = data[i]['agama']
                        alamat = data[i]['alamat']
                        gambar = data[i]['gambar']
                        kontak = data[i]['kontak']
                        jk = data[i]['jk']
                        if (status_rw == "diterima") {
                            rwCLass = "rw"
                        } else {
                            rwCLass = "rw-lock"
                        }
                        let html =
                            `
                        <tr>
                            <th scope="row">${no}</th>
                            <td>${jenis}</td>
                            <td><a href="/" type="button" data-bs-toggle="modal" data-bs-target="#info${code}"> ${nama}</a></td>
                            
                            <td>${tanggal}<br><p>${waktu}</p></td>
                            <td><p class="rt">${rt}</p></td>
                            <td><p class="${rwCLass}">${rw}</p></td>
                            <td><a class="btn izinkan-button" style="color: blue;" href="microsoft-edge:http://127.0.0.1:8000/static/file/${file}">Unduh</a></td>
                        </tr>
                        `
                        let html2 =
                            `
                        <div class="modal fade" id="info${code}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="exampleModalLabel">Pengurusan ${jenis}</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body row">
                                        <div class="col-6 mb-3">
                                            <p>Nama Pemohon : </p><p>${nama}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Kepala Keluarga : </p><p>${kepala}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>NIK Pemohon : </p><p>${nik}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Agama : </p><p>${agama}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Jenis Kelamin : </p><p>${jk}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Alamat : </p><p>${alamat}</p>
                                        </div>
                                        <div class="mb-3">
                                            <p>Kontak : </p><a href="https://wa.me/${kontak}">${kontak} (Click to check Whatsapp)</a>
                                        </div>
                                        <div class="mb-3">
                                            <p>Gambar Kartu Keluarga : </p><img src="../static/img/${gambar}" class="img-fluid d-block">
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">OK</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        `
                        $('#surat').prepend(html)
                        $('#simpan-modal').prepend(html2)
                        no = no + 1
                    }
                } else if (surat == "Surat Keterangan Tidak Mampu") {
                    rw = data[i]['rw']
                    jenis = data[i]['jenis_surat']
                    rt = data[i]['rt']
                    code = data[i]['code']
                    status_rw = data[i]['status-rw']
                    var lastUrl = window.location.href;
                    lastUrl = lastUrl.split("/")
                    if (rw == lastUrl[4] && status_rw == "diterima" && jenis == surat) {
                        nama = data[i]['nama']
                        tanggal = data[i]['tanggal_pengajuan']
                        waktu = data[i]['waktu_pengajuan']
                        status_rw = data[i]['status-rw']
                        kepala = data[i]['kepala']
                        nik = data[i]['nik']
                        agama = data[i]['agama']
                        alamat = data[i]['alamat']
                        gambar = data[i]['gambar']
                        kontak = data[i]['kontak']
                        jk = data[i]['jk']
                        if (status_rw == "diterima") {
                            rwCLass = "rw"
                        } else {
                            rwCLass = "rw-lock"
                        }
                        let html =
                            `
                        <tr>
                            <th scope="row">${no}</th>
                            <td>${jenis}</td>
                            <td><a href="/" type="button" data-bs-toggle="modal" data-bs-target="#info${code}"> ${nama}</a></td>
                            
                            <td>${tanggal}<br><p>${waktu}</p></td>
                            <td><p class="rt">${rt}</p></td>
                            <td><p class="${rwCLass}">${rw}</p></td>
                            <td><a class="btn izinkan-button" style="color: blue;" href="microsoft-edge:http://127.0.0.1:8000/static/file/${file}">Unduh</a></td>
                        </tr>
                        `
                        let html2 =
                            `
                        <div class="modal fade" id="info${code}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="exampleModalLabel">Pengurusan ${jenis}</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body row">
                                        <div class="col-6 mb-3">
                                            <p>Nama Pemohon : </p><p>${nama}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Kepala Keluarga : </p><p>${kepala}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>NIK Pemohon : </p><p>${nik}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Agama : </p><p>${agama}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Jenis Kelamin : </p><p>${jk}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Alamat : </p><p>${alamat}</p>
                                        </div>
                                        <div class="mb-3">
                                            <p>Kontak : </p><a href="https://wa.me/${kontak}">${kontak} (Click to check Whatsapp)</a>
                                        </div>
                                        <div class="mb-3">
                                            <p>Gambar Kartu Keluarga : </p><img src="../static/img/${gambar}" class="img-fluid d-block">
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">OK</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        `
                        $('#surat').prepend(html)
                        $('#simpan-modal').prepend(html2)
                        no = no + 1
                    }
                } else if (surat == "Surat Keterangan Kematian") {
                    rw = data[i]['rw']
                    jenis = data[i]['jenis_surat']
                    rt = data[i]['rt']
                    code = data[i]['code']
                    status_rw = data[i]['status-rw']
                    var lastUrl = window.location.href;
                    lastUrl = lastUrl.split("/")
                    if (rw == lastUrl[4] && status_rw == "diterima" && jenis == surat) {
                        nama = data[i]['nama']
                        tanggal = data[i]['tanggal_pengajuan']
                        waktu = data[i]['waktu_pengajuan']
                        status_rw = data[i]['status-rw']
                        kepala = data[i]['kepala']
                        nik = data[i]['nik']
                        agama = data[i]['agama']
                        alamat = data[i]['alamat']
                        gambar = data[i]['gambar']
                        kontak = data[i]['kontak']
                        jk = data[i]['jk']
                        if (status_rw == "diterima") {
                            rwCLass = "rw"
                        } else {
                            rwCLass = "rw-lock"
                        }
                        let html =
                            `
                        <tr>
                            <th scope="row">${no}</th>
                            <td>${jenis}</td>
                            <td><a href="/" type="button" data-bs-toggle="modal" data-bs-target="#info${code}"> ${nama}</a></td>
                            
                            <td>${tanggal}<br><p>${waktu}</p></td>
                            <td><p class="rt">${rt}</p></td>
                            <td><p class="${rwCLass}">${rw}</p></td>
                            <td><a class="btn izinkan-button" style="color: blue;" href="microsoft-edge:http://127.0.0.1:8000/static/file/${file}">Unduh</a></td>
                        </tr>
                        `
                        let html2 =
                            `
                        <div class="modal fade" id="info${code}" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h1 class="modal-title fs-5" id="exampleModalLabel">Pengurusan ${jenis}</h1>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body row">
                                        <div class="col-6 mb-3">
                                            <p>Nama Pemohon : </p><p>${nama}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Kepala Keluarga : </p><p>${kepala}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>NIK Pemohon : </p><p>${nik}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Agama : </p><p>${agama}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Jenis Kelamin : </p><p>${jk}</p>
                                        </div>
                                        <div class="col-6 mb-3">
                                            <p>Alamat : </p><p>${alamat}</p>
                                        </div>
                                        <div class="mb-3">
                                            <p>Kontak : </p><a href="https://wa.me/${kontak}">${kontak} (Click to check Whatsapp)</a>
                                        </div>
                                        <div class="mb-3">
                                            <p>Gambar Kartu Keluarga : </p><img src="../static/img/${gambar}" class="img-fluid d-block">
                                        </div>
                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">OK</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        `
                        $('#surat').prepend(html)
                        $('#simpan-modal').prepend(html2)
                        no = no + 1
                    }
                }
            }
        }
    })
});