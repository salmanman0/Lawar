function sign_in() {
    let username = $("#input-username").val();
    let password = $("#input-password").val();
    if (username === "") {
        $("#help-id-login").text("Silahkan masukkan username kamu");
        $("#input-password").focus();
        return;
    } else {
        $("#help-id-login").text("");
    }
    if (password === "") {
        $("#help-password-login").text("Please input your password.");
        $("#input-password").focus();
        return;
    } else {
        $("#help-password-login").text("");
    }
    $.ajax({
        type: "POST",
        url: "/sign_in",
        data: {
            username_give: username,
            password_give: password,
        },
        success: function (response) {
            if (response["result"] === "success") {
                $.cookie("mytoken", response["token"], {
                    path: "/"
                });
                // GET WAKTU
                var currentTime = new Date();
                var hours = currentTime.getHours();
                hours = (hours < 10 ? "0" : "") + hours;
                if (hours >= 4 && hours < 12) {
                    sapaan = "Pagi!";
                } else if (hours >= 12 && hours < 16) {
                    sapaan = "Siang!";
                } else if (hours >= 16 && hours < 19) {
                    sapaan = "Sore!";
                } else if (hours >= 19 || hours < 4) {
                    sapaan = "Malam!";
                }
                toastr.success('Selamat ' + sapaan + ' Semangat terus ya', 'Berhasil');
                setTimeout(function () {
                    window.location.replace("/");
                }, 1500);
            } else {
                toastr.error('Username atau Password Salah', 'Error');
            }
        },
    });
}