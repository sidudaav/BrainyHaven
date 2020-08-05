$(document).ready(function () {
    $('button.answer-btn').on("click", function (e) {
        answer = $(this).parent().find('h1.pattern-answer')
        answer.fadeToggle(100)

        var previous_action = $(this).data('action');

        // toggle data-action
        $(this).data('action', previous_action == 'view' ? 'close' : 'view');
        // toggle link text
        $(this).text(previous_action == 'view' ? 'Close Answer' : 'View Answer');
    });
});