document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('.alert-success')) {
        setTimeout(function() {
            document.querySelector('.alert-success').style.display = 'none';
        }, 5000);
    }
});