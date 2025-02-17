function initMap() {
  // --- <<<<<<<< --- Definiendo Variables --- >>>>>>>> ---
  let directionsService = new google.maps.DirectionsService();
  let directionsRenderer = new google.maps.DirectionsRenderer();

  let directionsServiceRet = new google.maps.DirectionsService();
  let directionsRendererRet = new google.maps.DirectionsRenderer();

  let directionsServiceIda = new google.maps.DirectionsService();
  let directionsRendererIda = new google.maps.DirectionsRenderer();

  // let center = new google.maps.LatLng(10.39698, -75.50265);
  const center = { lat: 10.39698, lng: -75.50265 };

  let start = document.getElementById("start");
  let end = document.getElementById("end");

  let start_ret = document.getElementById("start_ret");
  let end_ret = document.getElementById("end_ret");

  let start_ida = document.getElementById("start_ida");
  let end_ida = document.getElementById("end_ida");

  // --- <<<<<<<< --- Cree un cuadro delimitador con lados a ~150 km de distancia del punto central --- >>>>>>>> ---
  const defaultBounds = {
    north: center.lat + 0.1,
    south: center.lat - 0.1,
    east: center.lng + 0.1,
    west: center.lng - 0.1,
  };

  const start_a = document.getElementById("start_a");
  const end_a = document.getElementById("end_a");

  const start_b1 = document.getElementById("start_b1");
  const end_b1 = document.getElementById("end_b1");

  const start_b = document.getElementById("start_b");
  const end_b = document.getElementById("end_b");

  const options = {
    bounds: defaultBounds,
    componentRestrictions: { country: "co" },
    fields: ["address_components", "geometry", "icon", "name"],
    strictBounds: true,
  };

  const autocomplete_a = new google.maps.places.Autocomplete(start_a, options);
  const autocomplete_a2 = new google.maps.places.Autocomplete(end_a, options);

  const autocomplete_b1 = new google.maps.places.Autocomplete(
    start_b1,
    options
  );
  const autocomplete_b2_1 = new google.maps.places.Autocomplete(
    end_b1,
    options
  );

  const autocomplete_b = new google.maps.places.Autocomplete(start_b, options);
  const autocomplete_b2 = new google.maps.places.Autocomplete(end_b, options);

  autocomplete_a.setComponentRestrictions({
    country: ["co", "mx"],
  });
  autocomplete_a2.setComponentRestrictions({
    country: ["co", "mx"],
  });

  autocomplete_b.setComponentRestrictions({
    country: ["co", "mx"],
  });
  autocomplete_b2.setComponentRestrictions({
    country: ["co", "mx"],
  });

  autocomplete_b1.setComponentRestrictions({
    country: ["co", "mx"],
  });
  autocomplete_b2_1.setComponentRestrictions({
    country: ["co", "mx"],
  });

  // --- <<<<<<<< --- creando el mapa --- >>>>>>>> ---

  // const mapida = new google.maps.Map(document.getElementById("mapida"), {
  //   center: center,
  //   zoom: 12,
  //   mapTypeControl: false,
  // });

  const map = new google.maps.Map(document.getElementById("map"), {
    center: center,
    zoom: 12,
    mapTypeControl: false,
  });

  const mapret = new google.maps.Map(document.getElementById("mapret"), {
    center: center,
    zoom: 12,
    mapTypeControl: false,
  });

  // --- <<<<<<<< --- Autocompletador de lugares para el buscador --- >>>>>>>> ---

  // autocomplete_a.bindTo("bounds", map);

  // autocomplete_a.addListener("place_changed", () => {
  //   const info = new google.maps.place.PlaceResult();
  //   const place = autocomplete_a.getPlace(info);

  //   if (!place.geometry || !place.geometry.location) {
  //     return;
  //   }
  // });

  // --- <<<<<<<< --- Marca en el mapa la ruta uno--- >>>>>>>> ---
  directionsRenderer.setMap(map);
  const request = {
    origin: start.innerHTML,
    destination: end.innerHTML,
    travelMode: "DRIVING",
  };

  directionsService.route(request, (response) => {
    directionsRenderer.setDirections(response);
    showSteps(response);
  });

  // --- <<<<<<<< --- Marca en el mapa la ruta dos--- >>>>>>>> ---

  directionsRendererRet.setMap(mapret);
  const requestret = {
    origin: start_ret.innerHTML,
    destination: end_ret.innerHTML,
    travelMode: "DRIVING",
  };

  directionsServiceRet.route(requestret, (response) => {
    directionsRendererRet.setDirections(response);
    showStepsRet(response);
  });
}

function showSteps(directionResult) {
  const myRoute = directionResult.routes[0].legs[0];
  let distance = myRoute.distance;
  let duration = myRoute.duration;
  const dista = (document.getElementById("distanceId").value = distance.value);
  const durat = (document.getElementById("durationId").value = duration.value);
  const d_distancia = (document.getElementById("distancia-d").innerHTML =
    distance.text);
  const d_duracion = (document.getElementById("duracion-d").innerHTML =
    duration.text);
}

function showStepsRet(directionResult) {
  const myRouteRet = directionResult.routes[0].legs[0];
  let dist = myRouteRet.distance;
  let dur = myRouteRet.duration;
  let dista_r = (document.getElementById("distanceIdRet").value = dist.value);
  let durat_r = (document.getElementById("durationIdRet").value = dur.value);
  const d_distancia_d = (document.getElementById("distanciadb").innerHTML =
    dist.text);
  const d_duracion_d = (document.getElementById("duraciondb").innerHTML =
    dur.text);
}
