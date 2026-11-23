
document.addEventListener("DOMContentLoaded", function () {

    // Automatically hide flash messages after 4 seconds.
    const messages = document.querySelectorAll(".flash-message");

    messages.forEach(function (message) {
        setTimeout(function () {
            message.style.display = "none";
        }, 4000);
    });

    // Confirm before submitting a task completion form.
    const taskForms = document.querySelectorAll(
        'form[action*="/progress/"]'
    );

    taskForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const confirmed = confirm(
                "Do you want to update this task's status?"
            );

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

});
