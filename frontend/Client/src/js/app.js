import * as flsFunctions from './modules/functions.js';

flsFunctions.isWebp();

/*Меню бургер */

const burgerOpen = document.querySelector('.header__burger');
const burgerMenu = document.querySelector('.burger__menu');
const burgerClose = document.querySelector('.burger__menu__header-btn');
if (burgerOpen) {
  burgerOpen.addEventListener('click', () => {
    document.body.classList.toggle('_lock');
    burgerMenu.classList.toggle('_active');
  });
}
if (burgerClose) {
  burgerClose.addEventListener('click', () => {
    burgerMenu.classList.toggle('_active');
    document.body.classList.toggle('_lock');
  });
}

const slider = document.querySelector('.slider');
const scrollSpeed = 3;
let isDown = false;
let startX;
let scrollLeft = 0;

// EventListeners
slider.addEventListener('mousedown', (e) => {
  isDown = true;
  slider.classList.add('dragging');
  startX = e.pageX - slider.offsetLeft;
  scrollLeft = slider.scrollLeft;
});

slider.addEventListener('mouseup', () => {
  isDown = false;
  slider.classList.remove('dragging');
});

slider.addEventListener('mouseleave', () => {
  isDown = false;
  slider.classList.remove('dragging');
});

slider.addEventListener('mousemove', (e) => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - slider.offsetLeft;
  const walk = (x - startX) * scrollSpeed;
  slider.scrollLeft = scrollLeft - walk;
});
