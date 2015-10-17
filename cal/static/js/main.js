$(document).ready(function () {
    var current_month;
    $.ajax({
        url: "/month/2015",
        success: function (data) {
            var text = "";
            for (var key in data) {
                text += "<button class=\"month\" monthid=\"" + key + "\">" + data[key] + "</button>";
            }
            $("#months").html(text);
        }
    });

    var cal = $("#monthly-calendar").DataTable({
        ajax: {
            url: "/cal/2015/1",
            dataSrc: ""
        },
        "bFilter": false,
        "paging": false,
        "ordering": false,
        "info": false,
        "search": false
    });

    $("body").on("click", ".month", function () {
        var url = "/cal/2015/" + $(this).attr("monthid");
        cal.ajax.url(url).load();
    });

});
