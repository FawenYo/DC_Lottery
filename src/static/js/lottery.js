$(document).ready(function() {
    $("#lotteryBtn").click(function() {
        $(this).prop('disabled', true);
        $(this).css("display", "none");
        $("#loading_anim").css("display", "inline-block");
        lottery();
    });
});


function lottery() {
    const requestOptions = {
        method: 'GET',
        header: { 'Content-Type': 'application/json' },
        mode: 'cors'
    };

    let URL = "./api/lottery"

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
    $("#lotteryBtn").prop('disabled', false);
    $("#lotteryBtn").css("display", "inline");
    $("#loading_anim").css("display", "none");
}