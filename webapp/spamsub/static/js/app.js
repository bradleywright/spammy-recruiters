$("#SpammerForm").submit(function(event) {
    /* stop form from submitting normally */
    event.preventDefault();
    /* get some values from elements on the page */
    var $form = $(this),
    address = $form.find('input[name="address"]').val(),
    csrf = $form.find('input[name="csrf_token"]').val(),
    url = $form.attr('action');
    /* send the data using POST and re-generate the form w/the results */
    $.post(url, {
        address: address,
        csrf_token: csrf
        },
        function(data) {
            var content = $(data);
            $("#SpammerForm").html(content);
            $form.find('input[name="address"]').val("").focus();
            $("#thanks").delay(5000).fadeOut(500);
            $("#errors").delay(10000).fadeOut(750);
        }
    );
});
