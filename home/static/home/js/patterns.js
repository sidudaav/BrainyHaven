$(document).ready(function () {
    $('button.answer-btn').on("click", function (e) {
        answer = $(this).parent().find('.pattern-answer')

        var previous_action = $(this).data('action');

        if (previous_action == 'view') {
            answer.css({ "display": "inline-block" });
        } else {
            answer.css({ "display": "none" });
        }

        // toggle data-action
        $(this).data('action', previous_action == 'view' ? 'close' : 'view');
        // toggle link text
        $(this).text(previous_action == 'view' ? 'Close Answer' : 'View Answer');
    });
});