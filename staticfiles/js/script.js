document.addEventListener('DOMContentLoaded', function () {
    var exampleModal = document.getElementById('exampleModal');

    if (exampleModal) {
        exampleModal.addEventListener('show.bs.modal', function (event) {
            console.log('Modal is about to be shown');
        });

        exampleModal.addEventListener('hide.bs.modal', function (event) {
            console.log('Modal is about to be hidden');
        });
    } else {
        console.error('Modal element not found');
    }
});
