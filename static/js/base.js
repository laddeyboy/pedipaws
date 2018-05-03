$(function() {
  $(".toggleNav").on("click", function() {
    $(".flex-nav ul").toggleClass("open");
  });
});

function initMap() {
  var store = { lat: 29.753, lng: -95.339 };
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: store
  });
  var marker = new google.maps.Marker({
    position: store,
    map: map
  });
}

initMap();
// Contact modal
 $("#fade").modal({
  fadeDuration: 100
});