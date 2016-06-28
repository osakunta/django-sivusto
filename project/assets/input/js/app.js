// Takes a class name as a parameter and makes every container with said class
// as tall as the one of them which has the longest height.
function equalHeight(className) {
    $( document ).ready(function() {
        var heights = $(className).map(function() {
            return $(this).height();
        }).get(),

        maxHeight = Math.max.apply(null, heights);

        $(className).height(maxHeight);
    });
}

equalHeight(".equalize-footer");
equalHeight(".equalize-featured");
