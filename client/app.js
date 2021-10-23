


function getValue( name ) {
    var ui = document.getElementsByName(name);
    for(var i in ui) {
      if(ui[i].checked) {
          return parseInt(i);
      }
    }
    return -1; // Invalid Value
  }

function onClickedEstimatePrice() {

    var balcony = getValue("uiBalcony");
    var air_condition = getValue("uiAir");
    var parking = getValue("uiParking");
    var protected_room = getValue("uiProtected");
    var elevator = getValue("uiElevator");
    var sun_balcony = getValue("uiSun");
    var renovated = getValue("uiRenovated");
    var furnutire = getValue("uiFurnutire");
    var accesbilty = getValue("uiaccesbilty");
    var bars = getValue("uibars");
    var storage = getValue("uistorage");
    var house_area = document.getElementById("houseArea");
    var garden_area = document.getElementById("gardenArea");
    var rooms = document.getElementById("rooms");
    var city = document.getElementById("uiLocations");
    var neighborhood = document.getElementById("uiNeighborhoods");
    var house_type = document.getElementById("uiTypes");
        

    var url = "http://127.0.0.1:5000/predict_home_price"; 
    $.post(url, {
        city: city.value,
        neighborhood: neighborhood.value,
        houseType: house_type.value,
        houseArea: parseFloat(house_area.value),
        gardenArea: parseFloat(garden_area.value),
        rooms: parseFloat(rooms.value),
        balconies: parseFloat(balcony),
        airCondition: parseFloat(air_condition),
        parking: parseFloat(parking),
        protectedRoom: parseFloat(protected_room),
        elevator: parseFloat(elevator),
        sunBalcony: parseFloat(sun_balcony),
        renovated: parseFloat(renovated),
        furniture: parseFloat(furnutire),
        accessibility: parseFloat(accesbilty),
        bars: parseFloat(bars),
        storage : parseFloat(storage),

  }, function(data, status) {
      console.log(data.estimated_price);
      uiEstimatedPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " nis </h2>";
      console.log(status);
  });

}



function loadCities() {

  var url = "http://127.0.0.1:5000/get_location_names";
  $.get(url, function(data, status) {
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          $('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}

function loadHouseTypes() {

    var url = "http://127.0.0.1:5000/get_house_types";
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var types = data.types;
            var uiLocations = document.getElementById("uiTypes");
            $('#uiTypes').empty();
            for(var i in types) {
                var opt = new Option(types[i]);
                $('#uiTypes').append(opt);
            }
        }
    });
  }


  function loadNeighborhoods() {

    var url = "http://127.0.0.1:5000/get_neighborhoods";
    $.get(url, function(data, status) {
        if(data) {
            var locations = data.locations;
            var uiNeighborhoods = document.getElementById("uiNeighborhoods");
            $('#uiNeighborhoods').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiNeighborhoods').append(opt);
            }
        }
    });
  }

function load(){
    loadCities();
    loadHouseTypes();
    loadNeighborhoods();
}
window.onload = load;

