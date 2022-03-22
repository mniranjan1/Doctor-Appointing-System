$(document).ready(function() {
  $(".slider").slick({
    slidesToShow: 4,
    dots: true
  });
});

$(".carousel").carousel({
  interval: 2000,
  touch: true
});

$(document).ready(function() {
  $("#testimonial-slider").owlCarousel({
    items: 2,
    itemsDesktop: [1000, 2],
    itemsDesktopSmall: [979, 2],
    itemsTablet: [768, 1],
    pagination: true,
    navigation: false,
    autoplay: true
  });
});
