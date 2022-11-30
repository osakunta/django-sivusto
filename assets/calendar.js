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
    googleCalendarId: 'c_9d338487979b15952164e8f65f4904a79bfdc91ee3d99b8bd0ffd7f72fe0098f@group.calendar.google.com',
    className: 'gcal-sports',
  },
  {
    googleCalendarId: 'c_0e61cd901383f3d7ae9ff52f57dceae240a1dac3c9b5e426448b8751bf7f4bce@group.calendar.google.com',
    className: 'gcal-events',
  },
  {
    googleCalendarId: 'c_a2c54e1bc944a0ffeed775cf8568616bad5ab1141f1a7c4c3ca4cececd59754d@group.calendar.google.com',
    className: 'gcal-reserves',
  },
  {
    googleCalendarId: 'c_e0a144f6f0324c18dd1ac93ea19f20cac923aa7244672adad99a165f2e885c7d@group.calendar.google.com',
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
