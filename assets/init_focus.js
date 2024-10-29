document.addEventListener('DOMContentLoaded', function () {
    setTimeout(() => {
        const btn = document.getElementById('home-button');
        if (btn) {
            console.log('Button found, setting focus');
            btn.focus();
        } else {
            console.log('Button not found');
        }
    }, 500); // 500 milliseconds delay
});
