/*!
* Start Bootstrap - The Big Picture v5.0.6 (https://startbootstrap.com/template/the-big-picture)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-the-big-picture/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

$('#preview').on('change', function (e) {
    var reader = new FileReader();
    reader.onload = function (e) {
        $(".img--preview").attr('src', e.target.result);
    }
    reader.readAsDataURL(e.target.files[0]);
});
