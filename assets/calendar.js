import $ from 'jquery';
import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import googleCalendarPlugin from '@fullcalendar/google-calendar';
import listPlugin from '@fullcalendar/list';

// Bootstrap 3 md breakpoint.
const breakPoint = 992;

function monthCalendarView() {
  return window.innerWidth < breakPoint
    ? 'listMonth'
    : 'dayGridMonth';
}

function weekCalendarView() {
  return window.innerWidth < breakPoint
    ? 'listWeek'
    : 'dayGridWeek';
}

const googleCalendars = [
  {
    googleCalendarId: 'tqbg6bgc6r00hbs4p3bt6h1p4g@group.calendar.google.com',
    className: 'gcal-sports',
  },
  {
    googleCalendarId: 'c3f5fekmh2qfloegr4okfghk5k@group.calendar.google.com',
    className: 'gcal-service',
  },
  {
    googleCalendarId: 'boecmjgkjsuibnnj2op4c94ags@group.calendar.google.com',
    className: 'gcal-events',
  },
  {
    googleCalendarId: 'r151te2dmi4sfp130iahaj2vro@group.calendar.google.com',
    className: 'gcal-reserves',
  },
  {
    googleCalendarId: 'aojklsb36n1vpmesl2tqv1gp6o@group.calendar.google.com',
    className: 'gcal-meetings',
  },
];

const baseCalendarOptions = {
  plugins: [dayGridPlugin, googleCalendarPlugin, listPlugin],
  googleCalendarApiKey: 'AIzaSyDrE8zbaHSOjVVcoOPe00n7pSEYLv_ZKQM',
  eventSources: googleCalendars,
  locale: 'fi',
  firstDay: 1,
  eventTimeFormat: { hour12: false, hour: '2-digit', minute: '2-digit' },
  displayEventEnd: true,
  nextDayThreshold: '00:00:00',
  height: 'auto',
  eventDisplay: 'block',
}

const monthCalendarOptions = {
  ...baseCalendarOptions,
  initialView: monthCalendarView(),
  headerToolbar: {
    left: 'title',
    center: '',
    right: 'prev,next today'
  },
  windowResize: ({ view }) => view.calendar.changeView(monthCalendarView()),
}

const weekCalendarOptions = {
  ...baseCalendarOptions,
  initialView: weekCalendarView(),
  headerToolbar: {
    left: '',
    right: '',
  },
  windowResize: ({ view }) => view.calendar.changeView(weekCalendarView()),
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
}
