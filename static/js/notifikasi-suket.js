$(document).ready(function () {
    $('#pengajuan').val("")
    $('#key').val("")
})

document.getElementById('ajukan').addEventListener('click', function () {
    if ($('#nama').val() == "") {
        toastr.error('Waduh, kolom nama belum kamu isi', 'Error');
    } else if ($('#nik').val() == "") {
        toastr.error('Waduh, kolom nik belum kamu isi', 'Error');

    } else if ($('#ttl').val() == "") {
        toastr.error('Waduh, kolom Tempat Tanggal Lahir belum kamu isi', 'Error');

    } else if ($('#jk').val() == "") {
        toastr.error('Waduh, kolom Jenis Kelamin belum kamu isi', 'Error');

    } else if ($('#agama').val() == "") {
        toastr.error('Waduh, kolom agama belum kamu isi', 'Error');

    } else if ($('#status').val() == null) {
        toastr.error('Waduh, kolom status belum kamu isi', 'Error');

    } else if ($('#pekerjaan').val() == "") {
        toastr.error('Waduh, kolom pekerjaan belum kamu isi', 'Error');

    } else if ($('#pengajuan').val() == null) {
        toastr.error('Waduh, kolom Pengajuan Surat belum kamu isi', 'Error');

    } else if ($('#alamat').val() == "") {
        toastr.error('Waduh, kolom alamat belum kamu isi', 'Error');
    } else if ($('#nomorHP').val() == "") {
        toastr.error('Waduh, kolom Nomor HP belum kamu isi', 'Error');
    } else {
        if ($('#pengajuan').val() == "Surat Keterangan Tidak Mampu") {
            if ($('#keterangan').val() == "") {
                toastr.error('Waduh, kolom Keterangan belum kamu isi', 'Error');
            }
            else {
                $.ajax({
                    type: "POST",
                    url: "/data",
                    data: {
                        nama_give: $('#nama').val(),
                        nik_give: $('#nik').val(),
                        ttl_give: $('#ttl').val(),
                        jk_give: $('#jk').val(),
                        agama_give: $('#agama').val(),
                        pekerjaan_give: $('#pekerjaan').val(),
                        status_give: $('#status').val(),
                        alamat_give: $('#alamat').val(),
                        pengajuan_give: $('#pengajuan').val(),
                        nomorHP_give: $('#nomorHP').val(),
                        // keterangan surat
                        keterangan_give: $('#keterangan').val()
                    },
                    success: function (response) {
                        toastr.success(response['msg'], response['header']);
                        setTimeout(function () {
                            window.location.replace("/buat-surat");
                        }, 1500);
                    }
                })
            }
        }
        else if ($('#pengajuan').val() == "Surat Keterangan Kematian") {
            if ($('#nama_k').val() == "") {
                toastr.error('Waduh, kolom Nama Almarhum belum kamu isi', 'Error');
            }
            else if ($('#hubungan_k').val() == "") {
                toastr.error('Waduh, kolom Hubungan Dengan Almarhum belum kamu isi', 'Error');
            }
            else if ($('#nik_k').val() == "") {
                toastr.error('Waduh, kolom NIK Almarhum belum kamu isi', 'Error');
            }
            else if ($('#ttl_k').val() == "") {
                toastr.error('Waduh, kolom Tempat Tanggal Lahir Almarhum belum kamu isi', 'Error');
            }
            else if ($('#jk_k').val() == "") {
                toastr.error('Waduh, kolom Jenis Kelamin Almarhum belum kamu isi', 'Error');
            }
            else if ($('#agama_k').val() == "") {
                toastr.error('Waduh, kolom Agama Almarhum belum kamu isi', 'Error');
            }
            else if ($('#status_k').val() == "") {
                toastr.error('Waduh, kolom Status Perkawinan Almarhum belum kamu isi', 'Error');
            }
            else if ($('#pekerjaan_k').val() == "") {
                toastr.error('Waduh, kolom Pekerjaan Almarhum belum kamu isi', 'Error');
            }
            else if ($('#kewarganegaraan_k').val() == "") {
                toastr.error('Waduh, kolom Kewarganegaraan Almarhum belum kamu isi', 'Error');
            }
            else if ($('#hari_k').val() == "") {
                toastr.error('Waduh, kolom Hari Meninggal belum kamu isi', 'Error');
            }
            else if ($('#tanggal_k').val() == "") {
                toastr.error('Waduh, kolom Tanggal Meninggal belum kamu isi', 'Error');
            }
            else if ($('#pukul_k').val() == "") {
                toastr.error('Waduh, kolom Pukul Meninggal belum kamu isi', 'Error');
            }
            else if ($('#bertempat_k').val() == "") {
                toastr.error('Waduh, kolom Tempat Meninggal belum kamu isi', 'Error');
            }
            else if ($('#penyebab_k').val() == "") {
                toastr.error('Waduh, kolom Penyebab Meninggal belum kamu isi', 'Error');
            }
            else{
                $.ajax({
                    type: "POST",
                    url: "/data",
                    data: {
                        nama_give: $('#nama').val(),
                        nik_give: $('#nik').val(),
                        ttl_give: $('#ttl').val(),
                        jk_give: $('#jk').val(),
                        agama_give: $('#agama').val(),
                        pekerjaan_give: $('#pekerjaan').val(),
                        status_give: $('#status').val(),
                        alamat_give: $('#alamat').val(),
                        pengajuan_give: $('#pengajuan').val(),
                        nomorHP_give: $('#nomorHP').val(),
                        keterangan_give: $('#keterangan').val(),
                        // data yang meninggal
                        hubungan_k: $('#hubungan_k').val(),
                        nama_k: $('#nama_k').val(),
                        nik_k: $('#nik_k').val(),
                        ttl_k: $('#ttl_k').val(),
                        jk_k: $('#jk_k').val(),
                        agama_k: $('#agama_k').val(),
                        status_k: $('#status_k').val(),
                        pekerjaan_k: $('#pekerjaan_k').val(),
                        kewarganegaraan_k: $('#kewarganegaraan_k').val(),
                        alamat_k: $('#alamat_k').val(),
                        hari_k: $('#hari_k').val(),
                        tanggal_k: $('#tanggal_k').val(),
                        pukul_k: $('#pukul_k').val(),
                        bertempat_k: $('#bertempat_k').val(),
                        penyebab_k: $('#penyebab_k').val(),
                    },
                    success: function (response) {
                        toastr.success(response['msg'], response['header']);
                        setTimeout(function () {
                            window.location.replace("/buat-surat");
                        }, 1500);
                    }
                })
            }
        }
        else if ($('#pengajuan').val() == "Surat Keterangan Usaha") {
            if ($('#nama_u').val() == "") {
                toastr.error('Waduh, kolom Nama Usaha belum kamu isi', 'Error');
            }
            else if ($('#alamat_u').val() == "") {
                toastr.error('Waduh, kolom Alamat Usaha belum kamu isi', 'Error');
            }
            else {
                urusan = $('#tujuan').val()
                namaU = $('#nama_u').val()
                alamatU = $('#alamat_u').val()
                $.ajax({
                    type: "POST",
                    url: "/data",
                    data: {
                        nama_give: $('#nama').val(),
                        nik_give: $('#nik').val(),
                        ttl_give: $('#ttl').val(),
                        jk_give: $('#jk').val(),
                        agama_give: $('#agama').val(),
                        pekerjaan_give: $('#pekerjaan').val(),
                        status_give: $('#status').val(),
                        alamat_give: $('#alamat').val(),
                        pengajuan_give: $('#pengajuan').val(),
                        nomorHP_give: $('#nomorHP').val(),
                        // keterangan usaha
                        urusanU_give: urusan,
                        namaU_give: namaU,
                        alamatU_give: alamatU
                    },
                    success: function (response) {
                        toastr.success(response['msg'], response['header']);
                        setTimeout(function () {
                            window.location.replace("/buat-surat");
                        }, 1500);
                    }
                })
            }
        }
    }
})

document.getElementById('search-btn').addEventListener('click', function () {
    $.ajax({
        type: "GET",
        url: "/warga",
        data: {},
        success: function (response) {
            data = response['warga']
            rt_i = response['rt']
            rw_i = response['rw']
            key = $('#key').val()
            key = key.toUpperCase()
            for (let i = 0; i < data.length; i++) {
                nama = data[i]['nama']
                rt = data[i]['rt']
                rw = data[i]['rw']
                if (nama == key && rt == rt_i && rw == rw_i) {
                    $(".data").toggleClass("d-none d-block");
                    nik = data[i]['nik']
                    tgl_lahir = data[i]['tgl_lahir']
                    tmpt_lahir = data[i]['tmpt_lahir']
                    agama = data[i]['agama']
                    pekerjaan = data[i]['pekerjaan']
                    jk = data[i]['jk']
                    $('#nama').val(nama)
                    $('#nik').val(nik)
                    $('#ttl').val(tgl_lahir)
                    $('#jk').val(jk)
                    $('#agama').val(agama)
                    $('#pekerjaan').val(pekerjaan)
                    toastr.success('Data warga terkonfirmasi !', 'Berhasil');
                    break
                }
            }
            if (nama != key) {
                toastr.error(
                    'Maaf, data warga tidak ditemukan. Silahkan periksa kembali nama warga dan pastikan warga berada pada wilayah RT anda',
                    'Error');
            }
        }
    })
})

$("#pengajuan").change(function () {
    var surat = $(this).val();
    if (surat == "Surat Keterangan Tidak Mampu") {
        $('#miskin').show()
        $("#usaha_nama").hide()
        $("#usaha_alamat").hide()
        $("#usaha_tujuan").hide()
        $('#skk').hide()
    } else if (surat == "Surat Keterangan Usaha") {
        $("#miskin").hide()
        $("#usaha_nama").show()
        $("#usaha_alamat").show()
        $("#usaha_tujuan").show()
        $('#skk').hide()
    } else if (surat == "Surat Keterangan Kematian") {
        $("#miskin").hide()
        $("#usaha_nama").hide()
        $("#usaha_alamat").hide()
        $("#usaha_tujuan").hide()
        $('#skk').css({
            "display": "flex"
        })
    } else {
        $("#miskin").hide()
        $("#usaha_nama").hide()
        $("#usaha_alamat").hide()
        $("#usaha_tujuan").hide()
        $('#skk').hide()
    }
})