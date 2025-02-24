$(function () {
  $(".kslider").kslider({});
});

$(".kslider").kslider({
  animationSpeed: 500,
});

$(".kslider").kslider({
  pause: 3000,
});

$(".kslider").kslider({
  navigation: true,
});

$(".kslider").kslider({
  description: true,
});

$(".kslider").kslider({
  beforeDisplay: function (e, hiddenElement) {},
  afterDisplay: function (e, visibleElement) {},
});
