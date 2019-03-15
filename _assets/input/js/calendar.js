function CalendarOptions(eventSources) {
    this.eventSources = eventSources;
    this.googleCalendarApiKey = 'AIzaSyDrE8zbaHSOjVVcoOPe00n7pSEYLv_ZKQM';
    this.locale = 'fi';
    this.firstDay = 1;
    this.timeFormat = 'HH:mm';
    this.displayEventEnd = true;
    this.nextDayThreshold = '00:00:00';
    this.height = 'auto';
    this.header = {
        left:   'title',
        center: '',
        right:  'prev,next today'
    };

    // Estää tapahtumaa klikatessa Google-kalenterin aukeamisen ja näyttää tapahtuman
    // Bootstrap 3 modalissa. Modalin template on sato/templates/specific-pages/calendar-modal.html
    this.eventClick = function(event, jsEvent, view) {
        var start        = moment(event.start),
            end          = moment(event.end),
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
    };

    this.windowResize = function(view) {
        var ww = $(window).width(),
            view = $('#calendar').fullCalendar('getView');

        if (ww <= 768 && view.title !== 'listMonth'){
            $('#calendar').fullCalendar('changeView', 'listMonth');
        }

        if (ww > 768 && view.title !== 'month'){
            $('#calendar').fullCalendar('changeView', 'month');
        }
    };


    if ($(window).width() <= 768) {
        this.defaultView = 'listMonth';
    }
}

var eventCalendars = [
    {
        googleCalendarId: 'tqbg6bgc6r00hbs4p3bt6h1p4g@group.calendar.google.com',
        className: 'gcal-sports'
    }, {
        googleCalendarId: 'c3f5fekmh2qfloegr4okfghk5k@group.calendar.google.com',
        className: 'gcal-service'
    }, {
        googleCalendarId: 'boecmjgkjsuibnnj2op4c94ags@group.calendar.google.com',
        className: 'gcal-events'
    }, {
        googleCalendarId: 'r151te2dmi4sfp130iahaj2vro@group.calendar.google.com',
        className: 'gcal-reserves'
    }
];

var meetingCalendar = [
    {
        googleCalendarId: 'aojklsb36n1vpmesl2tqv1gp6o@group.calendar.google.com',
        className: 'gcal-meetings'
    }
];


$(document).ready(function() {
    // Poistetaan tiedot, kun modal suljetaan (estää bugin, jossa näytetään
    // edellisen tapahtuman tiedot, jos tietoja ei ole lainkaan)
    $('body').on('hidden.bs.modal', '.modal', function () {
        $('#fc-event-title').contents().remove();
        $('#fc-event-info').contents().remove();
        $('#fc-event-date').contents().remove();
        $('#fc-event-tile').removeAttr('href');
    });
});
