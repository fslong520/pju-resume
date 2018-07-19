function showElementsByWord(selector, char) {
    var char1 = char;
    var char2 = "";
    var char1Arr = char1.split('');
    var char1Arr2 = new Array()
    var i = 0

    $.each(char1Arr, function (index, j) {
        char2 += j;
        i += 1;
        char1Arr2[i] = char2;
    });
    for (i = 1; i < char1Arr2.length; i++) {
        a = char1Arr2[i];
        setH3(selector, i);
    }

    function setH3(selector, i) {
        setTimeout(function () {
            selector.html(char1Arr2[i]);
        }, i * 99);
    }
}

function showElementsByLine(selector, str, i) {
    if (selector == $("#contentbh3")) {
        i += 1; setTimeout(() => { selector.text(str); }, i * 100);
    }
    else {
        i += 1; setTimeout(() => { selector.html(str); }, i * 100);
    }

}

function showElementsByElement(selector, char, i) {
    setTimeout(function () {
        selector.html(char);
    }, i * 1000);
}
$(function () {
    showElementsByWord($("#contentbh3"), "今天我们来写一封简历！");
    showElementsByWord($("#contentlh3"), "这里将会展示个人基本信息。");
    showElementsByWord($("#contentrh3"), "这里将会展示个人简历详情。");

});
$(function () {
    setTimeout(() => {
        showElementsByWord($("#contentbh3"), "这里将会显示程序执行日志，就像控制台一样。");
    }, 1200);
    setTimeout(() => {
        showElementsByWord($("#contentbh3"), "那么我们开始吧!");
    }, 3500);
});