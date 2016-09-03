var calendarOptions = {
    googleCalendarApiKey: 'AIzaSyDrE8zbaHSOjVVcoOPe00n7pSEYLv_ZKQM',
    eventSources: [
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
        },
    ],
    firstDay: 1,
    timeFormat: 'HH:mm',
    displayEventEnd: true,
    nextDayThreshold: '00:00:00',
    height: 'auto',
    header: {
        left:   'title',
        center: '',
        right:  'prev,next today'
    },
    // Estää tapahtumaa klikatessa Google-kalenterin aukeamisen ja näyttää tapahtuman
    // Bootstrap 3 modalissa. Modalin template on sato/templates/specific-pages/calendar-modal.html
    eventClick: function(event, jsEvent, view) {
        var formatedDate = moment(event.start).format('DD.MM.') + " klo " + moment(event.start).format('HH:mm');

        // Erilainen formaatti, jos päättymispäivä on sama kuin alkamispäivä.
        if (parseInt(moment(event.start).format('DDMMYYYY')) == parseInt(moment(event.end).format('DDMMYYYY'))) {
            formatedDate += "–" + moment(event.end).format('HH:mm');
        } else{
            formatedDate += " – " + moment(event.end).format('DD.MM.') + " klo " + moment(event.end).format('HH:mm');
        }

        // Lisätään tiedot Bootstrap 3 modaliin
        $('#fc-event-title').html(event.title);
        $('#fc-event-title').attr('href', event.url);
        $('#fc-event-info').html(event.description);
        $('#fc-event-date').html(formatedDate);
        $('#fullCalModal').modal();
        return false;
    }
};

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
