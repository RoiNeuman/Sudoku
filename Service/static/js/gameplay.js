$('#startGame').click(function () {
    var level = $('#level').val();
    if(level > 81) {
        level = 81;
        $('#level').val(81);
    }
    $.get("/game/start/" + level, function (data, status) {
        var sudokugrid = "";
        for(i = 0; i < data.grid.length; i++) {
            var trstyle = "";
            if(i == 2 || i == 5) {
                trstyle = "border-bottom: 2px solid black;";
            }
            sudokugrid += "<tr id='tr-" + i + "' style='" + trstyle + "'>";
            for(j = 0; j < data.grid[i].length; j++) {
                var num = "&nbsp;&nbsp;";
                if(data.grid[i][j] != 0) {
                    num = data.grid[i][j];
                }
                if(j ==  2 || j == 5) {
                    tdstyle = "border: 1px solid black; border-right: 2px solid black;";
                } else {
                    tdstyle = "border: 1px solid black;";
                }
                var cellId = i*10 + j;
                sudokugrid += "<td style='" + tdstyle + "'><div id='" + cellId + "' row='" + i + "' column='" + j + "' class='cell'>" + num + "</div></td>";
            }
            sudokugrid += "</tr>";
        }
        $('#grid').html(sudokugrid);
        id = data._id;
        clickedRow = -1;
        clickedColumn = -1;
        $('#numbers').css('display', 'inline');
    });
});

$(document).on('click', '.cell', function () {
    var _id = $('.gridId').attr('id');
    var number = $(this).text();
    if(number == 0) {
        $('.cell').css('background-color', 'white');
        $(this).css('background-color', 'yellow');
        clickedRow = $(this).attr('row');
        clickedColumn = $(this).attr('column');
    }
});

$(document).on('click', '#numBtn', function () {
    var clickedNumber = $(this).text();
    if(clickedRow != -1) {
        $.ajax({
            type: 'POST',
            url: "/game/check",
            data: JSON.stringify({
                "id": id,
                "row": clickedRow,
                "column": clickedColumn,
                "number": clickedNumber
            }),
            error: function(e) {
                console.log(e);
            },
            dataType: "json",
            contentType: "application/json",
            success: function(data, status) {
                var cellId = parseInt(clickedRow)*10 + parseInt(clickedColumn);
                if(data.success) {
                    $("div[id='" + cellId + "']").css('background-color', 'green');
                    $("div[id='" + cellId + "']").text(clickedNumber);
                } else {
                    $("div[id='" + cellId + "']").css('background-color', 'red');
                }
            }
        });
    }
});