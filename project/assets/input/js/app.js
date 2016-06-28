//Makes footer content equal height
$( document ).ready(function() {
    var heights = $(".footer-equalize").map(function() {
        return $(this).height();
    }).get(),

    maxHeight = Math.max.apply(null, heights);

    $(".footer-equalize").height(maxHeight);
});
