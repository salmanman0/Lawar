var app = new Vue({
    el: "#app",
    data: {
        kk: null,
        warga: null,
        akun: null,
    },
    mounted: function () {
        fetch('103.150.191.178:5000/api/kk')
            .then(response => response.json())
            .then(data => {
                this.kk = data['kartu_keluarga'];
            });
        fetch('103.150.191.178:5000/warga')
            .then(response => response.json())
            .then(data => {
                this.warga = data['warga'];
            });
        fetch('103.150.191.178:5000/akun')
            .then(response => response.json())
            .then(data => {
                this.akun = data['akun'];
            });
    },
})