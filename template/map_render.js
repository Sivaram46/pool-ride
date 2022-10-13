function appendChildMultiple(parent, link) {
    //check function argument is an element
    if (parent.nodeType !== undefined) {
        const scriptTag = document.createElement("script");
        scriptTag.src = link
        // finally append child to parent
        parent.appendChild(scriptTag);
    }
}

appendChildMultiple(document.head, 'https://js.api.here.com/v3/3.1/mapsjs-core.js');
appendChildMultiple(document.head, 'https://js.api.here.com/v3/3.1/mapsjs-service.js')
appendChildMultiple(document.head, 'https://js.api.here.com/v3/3.1/mapsjs-mapevents.js')

const platform = new H.service.Platform({
    'apikey': 'GpDd-xA4yTAP0JdcIoNv0_BtCj_CbzFhUI75hRNdiRk'
});

// Obtain the default map types from the platform object:
const defaultLayers = platform.createDefaultLayers();

// Instantiate (and display) a map:
var map = new H.Map(
    document.getElementById("map"),
    defaultLayers.vector.normal.map, {
        zoom: 14,
        center: { lat: 52.5, lng: 13.4 }
    });

// MapEvents enables the event system
// Behavior implements default interactions for pan/zoom (also on mobile touch environments)
const behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
