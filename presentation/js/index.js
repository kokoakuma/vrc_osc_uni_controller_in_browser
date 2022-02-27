$(function() {
    $("#stick").draggable({
        containment: 'parent',
        scroll: false,
    });
});

$("#stick").on("dragstart", function(event, ui) {
    console.log("ドラッグ開始" + ui.position.top + ":" + ui.position.left);
});

// 200ミリ秒に一回しか呼ばれない
$("#stick").on("drag", _.throttle(function(event, ui) {
    console.log("ドラッグ中" + ui.position.top + ":" + ui.position.left);
    sendPosition(ui.position.top, ui.position.left)
}, 100));

$("#stick").on("dragstop", function(event, ui) {
    console.log("ドラッグ終了");
    stop()
    $(this).css({
        'left': "calc(50% - 32px)",
        'top': "calc(50% - 32px)"
    });
});

function sendPosition(top, left) {
    axios.post("/move", {
        top: top,
        left: left
    }).then(res => console.log("have successfully moved"))
}

function stop() {
    axios.post("/stop").then(res => console.log("have successfully stopped and done reset"))
}