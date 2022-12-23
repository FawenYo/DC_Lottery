$(document).ready(function() {
    $("#registerBtn").click(function() {
        $(this).prop('disabled', true);
        $(this).css("display", "none");
        $("#loading_anim").css("display", "inline-block");
        user_name = $("#user-name").val()
        register(user_name);
    });
});


function register(user_name) {
    let sendData = {
        "user_name": user_name,
    };

    const requestOptions = {
        method: 'POST',
        header: { 'Content-Type': 'application/json' },
        body: JSON.stringify(sendData),
        mode: 'cors'
    };

    let URL = "./api/register"

    fetch(URL, requestOptions)
        .then(response => response.json())
        .then((data) => {
            init(true)
            Swal.fire({
                icon: data.status,
                title: data.title,
                html: data.message,
                showLoaderOnConfirm: true,
                showCancelButton: false,
                confirmButtonText: '確定',
            })
        })
}

function init() {
    $("#registerBtn").prop('disabled', false);
    $("#registerBtn").css("display", "inline");
    $("#loading_anim").css("display", "none");
}