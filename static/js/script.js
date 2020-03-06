// Materialize Sidebar

$(document).ready(function () {
    $(".button-collapse").sideNav();
    $('.dropdown-button').dropdown();
    $('select').material_select();
});

// Search bar

$(document).ready(function() {

  $('.submit_on_enter').keydown(function(event) {
    // enter has keyCode = 13, change it if you want to use another button
    if (event.keyCode == 13) {
      this.form.submit();
      return false;
    }
  });

});

// Back to Top Button

if ($('#back-to-top').length) {
    var scrollTrigger = 100, // px
        backToTop = function () {
            var scrollTop = $(window).scrollTop();
            if (scrollTop > scrollTrigger) {
                $('#back-to-top').removeClass('scale-out');
            } else {
                $('#back-to-top').addClass('scale-out');
            }
        };
    backToTop();
    $(window).on('scroll', function () {
        backToTop();
    });

    $('#back-to-top').on('click', function (e) {
        e.preventDefault();
        $('html,body').animate({
            scrollTop: 0
        }, 700);
    });
}

// Modal to confirm the deletion of an exercise

window.onload = function() {
    var modal = document.getElementById("delete-modal");
    var btn = document.getElementById("delete-button");
    var span = document.getElementsByClassName("delete-close")[0];

    btn.onclick = function() {
        modal.style.display = "block";
    };

    span.onclick = function() {
        modal.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
};