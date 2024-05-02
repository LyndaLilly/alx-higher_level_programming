$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (xy) {
    $('DIV#hello').text(xy.hello);
  });
});
