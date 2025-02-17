function initMap() {
  let center = new google.maps.LatLng(10.39698, -75.50265);

  let start = document.getElementById("start");
  let end = document.getElementById("end");

  const defaultBounds = {
    north: center.lat + 0.15,
    south: center.lat - 0.15,
    east: center.lng + 0.15,
    west: center.lng - 0.15,
  };

  const start_a = document.getElementById("start_a");
  const end_a = document.getElementById("end_a");

  const options = {
    bounds: defaultBounds,
    componentRestrictions: { country: "co" },
    fields: ["address_components", "geometry", "icon", "name"],
    strictBounds: false,
  };

  const autocomplete_a = new google.maps.places.Autocomplete(start_a, options);
  const autocomplete_a2 = new google.maps.places.Autocomplete(end_a, options);

  autocomplete_a.setComponentRestrictions({
    country: ["co", "mx"],
  });
  autocomplete_a2.setComponentRestrictions({
    country: ["co", "mx"],
  });

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
}
