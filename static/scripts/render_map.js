const mapCenter = {lat:11.02488, lng:77.01021}
const API_KEY = "DCt7LzSN9sR8IGVpnTjD3CtQWYu55oinzBdFfD9idAE"

function moveMapToBerlin(map){
  map.setCenter(mapCenter);
  map.setZoom(14);
}
  
var platform = new H.service.Platform({
  apikey: API_KEY
});
var defaultLayers = platform.createDefaultLayers();

//Step 2: initialize a map - this map is centered over Europe
var map = new H.Map(document.getElementById('map'),
  defaultLayers.vector.normal.map,{
  center: mapCenter,
  zoom: 4,
  pixelRatio: window.devicePixelRatio || 1
});
// add a resize listener to make sure that the map occupies the whole container
window.addEventListener('resize', () => map.getViewPort().resize());

//Step 3: make the map interactive
// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

// Create the default UI components
var ui = H.ui.UI.createDefault(map, defaultLayers);
  
// Focus out listener for source and destination form elements
const source = document.getElementById('source')
const dest = document.getElementById('dest')

const latlngs = []

function addMarkersToMap(map, coords) {
  var marker = new H.map.Marker(coords);
  console.log(coords);
  map.addObject(marker);
}

function inputFocusOut() {
  if (source.value.length) {
    console.log('Source Focus out');
    
    fetch(`https://geocode.search.hereapi.com/v1/geocode?q=${source.value}&apiKey=${API_KEY}`)
    .then((response) => response.json())
    .then(function(source_res) {
      if (source_res.items != undefined && source_res.items.length) {

        addMarkersToMap(map, {
          lat: source_res.items[0].position.lat, 
          lng: source_res.items[0].position.lng
        });
      }
    })
  }
}

source.addEventListener("focusout", inputFocusOut);

// Now use the map as required...
window.onload = function () {
  moveMapToBerlin(map);
  addMarkersToMap(map, mapCenter);
}

