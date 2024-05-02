$('document').ready(function () {
  const link = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(function () {
    $.get(link + $.param({ lang: $('INPUT#language_code').val() }), function (xy) {
      $('DIV#hello').html(xy.hello);
    });
  });
});
