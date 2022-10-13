var platform = new H.service.Platform({
  apikey: '4zrYS3HwHMWmrB6jcbGjNRltDgVws9KsQXl_BD4wHgs'
});

var defaultLayers = platform.createDefaultLayers();

var map = new H.Map(document.getElementById('map'),
  defaultLayers.vector.normal.map,{
  center: {lat:11.02488, lng:77.01021},
  zoom: 18,
  pixelRatio: window.devicePixelRatio || 1
});

window.addEventListener('resize', () => map.getViewPort().resize());

//Step 3: make the map interactive
// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

// Create the default UI components
var ui = H.ui.UI.createDefault(map, defaultLayers);

const autosuggest_source = (e) => {
  if(event.metaKey){
    return
  }

let searchString = e.value
if (searchString != "") {
  fetch(
    `https://autosuggest.search.hereapi.com/v1/autosuggest?apiKey=DCt7LzSN9sR8IGVpnTjD3CtQWYu55oinzBdFfD9idAE&at=33.738045,73.084488&limit=2&resultType=city&q=${searchString}&lang=en-US`
  )
  .then((res) => res.json())
  .then((json) => {
    if (json.length != 0) {
      document.getElementById("list_source").innerHTML = ``;
      let dropData = json.items.map((item) => {
        if ((item.position != undefined) & (item.position != ""))
          document.getElementById("list_source").innerHTML += `<li onClick="addMarkerToMapSource(${item.position.lat},${item.position.lng},'${item.title}')">${item.title}</li>`;
      });
    }
  });
}
};

const addMarkerToMapSource = (lat, lng, title) => {
  // map.removeObjects(map.getObjects())
  document.getElementById("source").value = title;
  document.getElementById("source_pts").value = `${lat}, ${lng}`

  const svgMarkup = '<svg height="100" width="100" xmlns="http://www.w3.org/2000/svg">' +
  '<circle cx="50" cy="50" r="20" stroke="black" stroke-width="3" fill="red" /></svg>';
  const customIcon = new H.map.Icon(svgMarkup);
  var selectedLocationMarker = new H.map.Marker({ lat, lng }, {icon: customIcon});
  map.addObject(selectedLocationMarker);
  document.getElementById("list_source").innerHTML = ``;
  map.setCenter({ lat, lng }, true); 
};  

const autosuggest_dest = (e) => {
  if(event.metaKey){
    return
  }

let searchString = e.value
if (searchString != "") {
  fetch(
    `https://autosuggest.search.hereapi.com/v1/autosuggest?apiKey=DCt7LzSN9sR8IGVpnTjD3CtQWYu55oinzBdFfD9idAE&at=33.738045,73.084488&limit=2&resultType=city&q=${searchString}&lang=en-US`
  )
  .then((res) => res.json())
  .then((json) => {
    if (json.length != 0) {
      document.getElementById("list_dest").innerHTML = ``;
      let dropData = json.items.map((item) => {
        if ((item.position != undefined) & (item.position != ""))
          document.getElementById("list_dest").innerHTML += `<li onClick="addMarkerToMapDest(${item.position.lat},${item.position.lng},'${item.title}')">${item.title}</li>`;
      });
    }
  });
}
};

const addMarkerToMapDest = (lat, lng, title) => {
  // map.removeObjects(map.getObjects())
  document.getElementById("dest").value = title;
  document.getElementById("dest_pts").value = `${lat}, ${lng}`;

  const svgMarkup = '<svg height="100" width="100" xmlns="http://www.w3.org/2000/svg">' +
  '<circle cx="50" cy="50" r="20" stroke="black" stroke-width="3" fill="green" /></svg>';
  const customIcon = new H.map.Icon(svgMarkup);
  var selectedLocationMarker = new H.map.Marker({ lat, lng }, {icon: customIcon});

  map.addObject(selectedLocationMarker);
  document.getElementById("list_dest").innerHTML = ``;
  map.setCenter({ lat, lng }, true); 
};  