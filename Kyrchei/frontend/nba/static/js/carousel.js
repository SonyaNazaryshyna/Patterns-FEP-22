const track = document.querySelector('.carousel-track');
const items = document.querySelectorAll('.carousel-item');
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');
let currentIndex = 0;

function updateCarousel() {
     const offset = -currentIndex * 100;
     track.style.transform = `translateX(${offset}%)`;
}

nextButton.addEventListener('click', () => {
     currentIndex = (currentIndex + 1) % items.length;
     updateCarousel();
});

prevButton.addEventListener('click', () => {
     currentIndex = (currentIndex - 1 + items.length) % items.length;
     updateCarousel();
});