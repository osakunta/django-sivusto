import $ from 'jquery';
import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import googleCalendarPlugin from '@fullcalendar/google-calendar';
import listPlugin from '@fullcalendar/list';

const eventCalendars = [
  {
    googleCalendarId: 'tqbg6bgc6r00hbs4p3bt6h1p4g@group.calendar.google.com',
    className: 'gcal-sports'
  },
  {
    googleCalendarId: 'c3f5fekmh2qfloegr4okfghk5k@group.calendar.google.com',
    className: 'gcal-service'
  },
  {
    googleCalendarId: 'boecmjgkjsuibnnj2op4c94ags@group.calendar.google.com',
    className: 'gcal-events'
  },
  {
    googleCalendarId: 'r151te2dmi4sfp130iahaj2vro@group.calendar.google.com',
    className: 'gcal-reserves'
  }
];

const meetingCalendar = [
  {
    googleCalendarId: 'aojklsb36n1vpmesl2tqv1gp6o@group.calendar.google.com',
    className: 'gcal-meetings'
  }
];

const baseCalendarOptions = {
  plugins: [dayGridPlugin, googleCalendarPlugin, listPlugin],
  googleCalendarApiKey: 'AIzaSyDrE8zbaHSOjVVcoOPe00n7pSEYLv_ZKQM',
  locale: 'fi',
  firstDay: 1,
  eventTimeFormat: { hour12: false, hour: '2-digit', minute: '2-digit' },
  displayEventEnd: true,
  nextDayThreshold: '00:00:00',
  height: 'auto',

  // Estää tapahtumaa klikatessa Google-kalenterin aukeamisen ja näyttää tapahtuman
  // Bootstrap 3 modalissa. Modalin template on sato/templates/specific-pages/calendar-modal.html
  eventClick: function (event, jsEvent, view) {
    var start = moment(event.start),
      end = moment(event.end),
      formatedDate = start.format('DD.MM.') + " klo " + start.format('HH:mm');

    // Erilainen formaatti, jos päättymispäivä on sama kuin alkamispäivä.
    if (start.format('DDMMYYYY') === end.format('DDMMYYYY')) {
      formatedDate += "–" + end.format('HH:mm');
    } else if (end.format('DDMMYYYY') !== 'Invalid date') {
      formatedDate += " – " + end.format('DD.MM.') + " klo " + end.format('HH:mm');
    }

    // Lisätään tiedot Bootstrap 3 modaliin
    $('#fc-event-title').html(event.title);
    $('#fc-event-title').attr('href', event.url);
    $('#fc-event-info').html(event.description);
    $('#fc-event-date').html(formatedDate);
    $('#fullCalModal').modal();
    return false;
  },
}

const monthCalendarOptions = {
  ...baseCalendarOptions,
  eventSources: [...eventCalendars, ...meetingCalendar],
  headerToolbar: {
    left: 'title',
    center: '',
    right: 'prev,next today'
  },
  /*   windowResize: function (_) {
      const ww = $(window).width();
      const view = $('#calendar').fullCalendar('getView');
  
      if (ww <= 768 && view.title !== 'listMonth') {
        $('#calendar').fullCalendar('changeView', 'listMonth');
      }
  
      if (ww > 768 && view.title !== 'month') {
        $('#calendar').fullCalendar('changeView', 'month');
      }
    }, */
}

const weekCalendarOptions = {
  ...baseCalendarOptions,
  initialView: 'dayGridWeek',
  eventSources: eventCalendars,
  headerToolbar: {
    left: '',
    right: '',
  },
  /*   windowResize: function (_) {
      const ww = $(window).width();
      const view = $('#calendar').fullCalendar('getView');
    
      if (ww <= 768 && view.title !== 'listWeek') {
        $('#calendar').fullCalendar('changeView', 'listWeek');
      }
    
      if (ww > 768 && view.title !== 'basicWeek') {
        $('#calendar').fullCalendar('changeView', 'basicWeek');
      }
    }, */
}

export default function calendar(isWeekCalendar) {
  const calendarOptions = isWeekCalendar
    ? weekCalendarOptions
    : monthCalendarOptions;

  const calendarEl = document.getElementById('calendar');

  const calendar = new Calendar(
    calendarEl,
    calendarOptions,
  );

  calendar.render();

  // Poistetaan tiedot, kun modal suljetaan (estää bugin, jossa näytetään
  // edellisen tapahtuman tiedot, jos tietoja ei ole lainkaan)
  $('body').on('hidden.bs.modal', '.modal', function () {
    $('#fc-event-title').contents().remove();
    $('#fc-event-info').contents().remove();
    $('#fc-event-date').contents().remove();
    $('#fc-event-tile').removeAttr('href');
  });
}
