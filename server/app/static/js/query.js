$(document).ready(function(e) {

  $('.ui.form').form({
    fields: {
      name: ['empty', 'maxLength[50]'],
    }
  })

});

