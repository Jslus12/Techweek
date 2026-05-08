'use strict';

// ─────────────────────────────────────────────
// 1. NAVBAR SLIDE IN
// ─────────────────────────────────────────────
(function initNavbar() {
    const nav = document.getElementById('navbar');
    setTimeout(() => nav.classList.add('visible'), 200);
})();


// ─────────────────────────────────────────────
// 3. SCROLL REVEAL — animações simplificadas
// ─────────────────────────────────────────────
(function initReveal() {
    const elements = document.querySelectorAll('[data-reveal]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el    = entry.target;
            const delay = parseInt(el.dataset.delay || 0);

            setTimeout(() => {
                el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                el.style.opacity    = '1';
                el.style.transform  = 'none';

                if (el.classList.contains('hero-line')) {
                    el.style.transition += ', width 0.8s ease';
                    el.style.width = '60%';
                }
            }, delay);

            observer.unobserve(el);
        });
    }, { threshold: 0.15 });

    elements.forEach(el => observer.observe(el));
})();


// ─────────────────────────────────────────────
// 4. FAQ ACCORDION
// ─────────────────────────────────────────────
(function initAccordion() {
    const triggers = document.querySelectorAll('.faq-trigger');

    triggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const isOpen = trigger.getAttribute('aria-expanded') === 'true';
            const body   = trigger.nextElementSibling;

            // Fecha os outros
            triggers.forEach(t => {
                if (t !== trigger) {
                    t.setAttribute('aria-expanded', 'false');
                    t.nextElementSibling.classList.remove('open');
                }
            });

            // Alterna o atual
            trigger.setAttribute('aria-expanded', String(!isOpen));
            body.classList.toggle('open', !isOpen);
        });
    });
})();


// ─────────────────────────────────────────────
// 5. FAQ ITEMS — reveal escalonado
// ─────────────────────────────────────────────
(function initFaqReveal() {
    const items = document.querySelectorAll('.faq-item[data-reveal]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el    = entry.target;
            const delay = parseInt(el.dataset.delay || 0) + 200;
            setTimeout(() => {
                el.style.transition = 'opacity 0.45s ease, transform 0.45s ease';
                el.style.opacity    = '1';
                el.style.transform  = 'translateY(0)';
            }, delay);
            observer.unobserve(el);
        });
    }, { threshold: 0.1 });

    items.forEach(el => observer.observe(el));
})();


// ─────────────────────────────────────────────
// 6. CONTACT STRIP REVEAL
// ─────────────────────────────────────────────
(function initContactReveal() {
    const strip = document.querySelector('.contact-strip[data-reveal]');
    if (!strip) return;

    const observer = new IntersectionObserver(([entry]) => {
        if (!entry.isIntersecting) return;
        const delay = parseInt(strip.dataset.delay || 0) + 300;
        setTimeout(() => {
            strip.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            strip.style.opacity    = '1';
            strip.style.transform  = 'none';
        }, delay);
        observer.unobserve(strip);
    }, { threshold: 0.2 });

    observer.observe(strip);
})();