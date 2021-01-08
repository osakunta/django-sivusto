import $ from 'jquery';

// function to set the height on fly so footer stays on the bottom of the page.
function autoHeight() {
  $('#content').css('min-height', 0);
  $('#content').css('min-height', (
    $(document).height()
    - $('#header').outerHeight()
    - $('#footer').outerHeight()
    - $('#cms-top .cms-toolbar').outerHeight()
  ));
}

export default function app() {
  autoHeight();

  $(window).resize(function () {
    autoHeight();
  });

  $(function () {
    $('[data-toggle="tooltip"]').tooltip({
      'trigger': 'hover focus'
    })
  });
}
