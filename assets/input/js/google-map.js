var map;

function initMap() {
    var coords = {
        lat: 60.1671291,
        lng: 24.9252689
    };

    map = new google.maps.Map(document.getElementById('map'), {
        center: coords,
        zoom: 13
    });

    var marker = new google.maps.Marker({
        position: coords,
        map: map,
        title: 'SatO'
      });

}
