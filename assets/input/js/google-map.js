var map;

function initMap() {
    var coords = {
        lat: 60.1671291,
        lng: 24.9252689
    };

    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15
    });

    var geocoder = new google.maps.Geocoder();
    var address = "Lapinrinne 1 A 8, Helsinki";

    geocoder.geocode({'address': address}, function(results, status) {
        if (status === 'OK') {
            map.setCenter(results[0].geometry.location);

            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });


}
