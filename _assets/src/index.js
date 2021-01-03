import $ from 'jquery';
import 'bootstrap';

import app from './app';
import calendar from './calendar';

function main() {
  const splitPath = window.location.pathname.split('/');
  const page = splitPath[2];
  const subPage = splitPath[3];

  app();

  switch (page) {
    case '':
      calendar(true);
    case 'osakunta':
      switch (subPage) {
        case 'kalenteri': calendar(false);
      }
  }
}

$(document).ready(function () {
  main();
});
