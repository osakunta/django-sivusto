// Takes a class name as a parameter and makes every container with said class
// as tall as the tallest of them.
function equalHeight(className) {
    var heights;
    
    $(className).removeAttr("style");

    heights = $(className).map(function() {
        return $(this).height();
    }).get(),
        
    maxHeight = Math.max.apply(null, heights);

    $(className).height(maxHeight);
}


// function to set the height on fly
function autoHeight() {
    $('#content').css('min-height', 0);
    $('#content').css('min-height', (
        $(document).height() 
        - $('#header').outerHeight() 
        - $('#footer').outerHeight()
    ));
    
}

// onDocumentReady function bind
$(document).ready(function() {
    autoHeight();
    equalHeight(".equalize-footer");
    equalHeight(".equalize-featured");
});

// onResize bind of the function
$(window).resize(function() {
    autoHeight();
    equalHeight(".equalize-footer");
    equalHeight(".equalize-featured");
});

