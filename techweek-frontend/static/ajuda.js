'use strict';

// Navbar
setTimeout(() => document.getElementById('navbar').classList.add('visible'), 100);

// Hero
document.querySelector('.hero-label').classList.add('show');
document.querySelector('.hero-title').classList.add('show');
document.querySelector('.hero-sub').classList.add('show');
document.querySelector('.hero-line').classList.add('show');

// FAQ items — fade escalonado
document.querySelectorAll('.faq-item').forEach((item, i) => {
    setTimeout(() => item.classList.add('show'), i * 80);
});

// Contact strip
setTimeout(() => {
    const strip = document.querySelector('.contact-strip');
    if (strip) strip.classList.add('show');
}, 300);

// Accordion
document.querySelectorAll('.faq-trigger').forEach(trigger => {
    trigger.addEventListener('click', () => {
        const isOpen = trigger.getAttribute('aria-expanded') === 'true';
        document.querySelectorAll('.faq-trigger').forEach(t => {
            t.setAttribute('aria-expanded', 'false');
            t.nextElementSibling.classList.remove('open');
        });
        trigger.setAttribute('aria-expanded', String(!isOpen));
        trigger.nextElementSibling.classList.toggle('open', !isOpen);
    });
});