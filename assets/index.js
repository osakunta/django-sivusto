import $ from 'jquery';
import 'bootstrap-sass';
import "@fortawesome/fontawesome-free/js/all";
import "@fortawesome/fontawesome-free/css/all.css";
import "./sass/styles.sass";
import "./img/favicon.ico";
import "./img/logos/main.png";
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
