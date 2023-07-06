$(document).ready(function() {
    $('#btnBuscarUsuarios').click(function() {
    $.ajax({
        url: 'https://randomuser.me/api/',
        dataType: 'json',
        success: function(data) {
          // Procesar los datos de respuesta y mostrarlos en la página
        var usuario = data.results[0];
        var nombre = usuario.name.first + ' ' + usuario.name.last;
        var correo = usuario.email;
        var imagen = usuario.picture.large;

          // Crear un elemento de imagen
        var imagenElemento = $('<img>').attr('src', imagen);

          // Crear elementos de párrafo para el nombre y el correo
        var nombreElemento = $('<p>').text('Nombre: ' + nombre);
        ;

          // Vaciar el contenedor de resultados
        $('#resultados').empty();

          // Agregar los elementos al contenedor de resultados
        $('#resultados').append(imagenElemento, nombreElemento,correo);
        }
    });
    });
});