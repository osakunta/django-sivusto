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

// Settings for Instafeed.js
// var satoInstafeed = new Instafeed({
//   get: 'user',
//   userId: '1500056937',
//   clientId: '26baf6a598e64f5e86bf6369e849f3eb',
//   accessToken: '1500056937.1677ed0.9dc272018f224b0fa4cf75dc26209c49',
//   limit: 6
// });

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
