document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.review-btn');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const reviewText = button.getAttribute('data-review');
            document.getElementById('reviewText').innerText = reviewText;
            document.getElementById('reviewPopup').style.display = 'flex';
        });
    });
});

function closePopup() {
    document.getElementById('reviewPopup').style.display = 'none';
}
