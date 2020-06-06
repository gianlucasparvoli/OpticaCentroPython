//token: pk.eyJ1IjoiZ3NwYXJ2b2xpIiwiYSI6ImNrM3QyODBuNTBkZDczY2xxY3hsbHA1dDkifQ.3Tj2FFQImwC2AcfjZEmmwQ
//-33.3301369,-60.2187023

mapboxgl.accessToken = 'pk.eyJ1IjoiZ3NwYXJ2b2xpIiwiYSI6ImNrM3QyODBuNTBkZDczY2xxY3hsbHA1dDkifQ.3Tj2FFQImwC2AcfjZEmmwQ';

let map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-60.2187023, -33.3301369],
    zoom: 15,
    doubleClickZoom: true
});

let element = document.createElement('div');
element.className = 'marker';

let marker = new mapboxgl.Marker(element).setLngLat({
    lng: -60.2187023,
    lat: -33.3301369
}).addTo(map);