src = "https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js";

// $(function() {
//   $(".toggleNav").on("click", function() {
//     $(".flex-nav ul").toggleClass("open");
//   });
// });

function initMap() {
    var uluru = {lat: -25.363, lng: 131.044};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: uluru
    });
    var marker = new google.maps.Marker({
      position: uluru,
      map: map
    });
}

initMap();
