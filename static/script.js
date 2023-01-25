$(document).ready(function () {
    $(".list-group-item-action").click(function () {
        let product_id = $(this).attr('id');
        $.get("http://127.0.0.1:8000/product/" + product_id + "/")
            .then(function (result){
                // $(조건).attr("src", 값)
                $("#detailModalImage").attr("src", result.image);
                $("#detailModalTitle").text(result.title);
                $("#detailModalUsername").text(result.username);
                $("#detailModalLocation").text(result.location);
                $("#detailModalPrice").text(result.price);
                $("#detailModalContent").html(result.content);
                $("#detailModal").modal("show");
            })
    });
});