/* =============================================
   WEEKTECH 2026 — ajuda.js
   All animations & interactions
   ============================================= */

'use strict';

// ─────────────────────────────────────────────
// 1. CANVAS BACKGROUND  (particles + shooting rays)
// ─────────────────────────────────────────────
(function initCanvas() {
    const canvas = document.getElementById('bg-canvas');
    const ctx    = canvas.getContext('2d');

    let W, H;

    function resize() {
        W = canvas.width  = window.innerWidth;
        H = canvas.height = window.innerHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    // ── Particles ──
    const PARTICLE_COUNT = 90;
    const particles = [];

    class Particle {
        constructor() { this.reset(true); }

        reset(randomY = false) {
            this.x  = Math.random() * W;
            this.y  = randomY ? Math.random() * H : H + 4;
            this.vy = -(0.15 + Math.random() * 0.5);
            this.vx = (Math.random() - 0.5) * 0.15;
            this.r  = 0.5 + Math.random() * 1.2;
            this.a  = 0;
            this.aTarget = 0.2 + Math.random() * 0.5;
            this.life = 0;
            this.maxLife = 200 + Math.random() * 300;
        }

        update() {
            this.life++;
            const t = this.life / this.maxLife;
            // fade in/out
            this.a = t < 0.1 ? (t / 0.1) * this.aTarget
                   : t > 0.8 ? ((1 - t) / 0.2) * this.aTarget
                   : this.aTarget;
            this.x += this.vx;
            this.y += this.vy;
            if (this.life >= this.maxLife) this.reset();
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0,212,255,${this.a.toFixed(2)})`;
            ctx.fill();
        }
    }

    for (let i = 0; i < PARTICLE_COUNT; i++) particles.push(new Particle());

    // ── Shooting rays ──
    const rays = [];

    class Ray {
        constructor() { this.reset(); }

        reset() {
            this.x  = Math.random() * W;
            this.y  = Math.random() * H * 0.5;
            this.len  = 60 + Math.random() * 180;
            this.angle = Math.PI / 2 + (Math.random() - 0.5) * 0.4;
            this.speed = 4 + Math.random() * 6;
            this.progress = 0;
            this.opacity = 0.3 + Math.random() * 0.4;
            this.delay = Math.random() * 240;
            this.countdown = this.delay;
            this.done = false;
        }

        update() {
            if (this.countdown > 0) { this.countdown--; return; }
            this.progress += this.speed;
            if (this.progress > this.len + 60) this.done = true;
        }

        draw() {
            if (this.countdown > 0) return;
            const start = Math.max(0, this.progress - this.len);
            const end   = this.progress;
            const dx    = Math.cos(this.angle);
            const dy    = Math.sin(this.angle);

            const x1 = this.x + dx * start;
            const y1 = this.y + dy * start;
            const x2 = this.x + dx * end;
            const y2 = this.y + dy * end;

            const grad = ctx.createLinearGradient(x1, y1, x2, y2);
            grad.addColorStop(0, `rgba(0,212,255,0)`);
            grad.addColorStop(0.5, `rgba(0,212,255,${this.opacity})`);
            grad.addColorStop(1, `rgba(0,212,255,0)`);

            ctx.beginPath();
            ctx.moveTo(x1, y1);
            ctx.lineTo(x2, y2);
            ctx.strokeStyle = grad;
            ctx.lineWidth = 1.2;
            ctx.stroke();
        }
    }

    // Spawn rays periodically
    let rayTimer = 0;
    const RAY_INTERVAL = 40;

    function spawnRay() {
        rays.push(new Ray());
        // cap pool
        if (rays.length > 20) rays.splice(0, rays.length - 20);
    }

    // ── Grid lines (subtle) ──
    function drawGrid() {
        ctx.strokeStyle = 'rgba(0,212,255,0.025)';
        ctx.lineWidth   = 1;
        const step = 80;
        for (let x = 0; x < W; x += step) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke();
        }
        for (let y = 0; y < H; y += step) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke();
        }
    }

    // ── Central glow ──
    function drawGlow() {
        const cx = W / 2, cy = H * 0.28;
        const grad = ctx.createRadialGradient(cx, cy, 0, cx, cy, 320);
        grad.addColorStop(0, 'rgba(0,212,255,0.06)');
        grad.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(cx, cy, 320, 0, Math.PI * 2);
        ctx.fill();
    }

    // ── Main loop ──
    function tick() {
        ctx.clearRect(0, 0, W, H);

        drawGrid();
        drawGlow();

        particles.forEach(p => { p.update(); p.draw(); });

        rayTimer++;
        if (rayTimer % RAY_INTERVAL === 0) spawnRay();

        for (let i = rays.length - 1; i >= 0; i--) {
            rays[i].update();
            rays[i].draw();
            if (rays[i].done) rays.splice(i, 1);
        }

        requestAnimationFrame(tick);
    }

    tick();
})();


// ─────────────────────────────────────────────
// 2. CURSOR GLOW
// ─────────────────────────────────────────────
(function initCursor() {
    const glow = document.getElementById('cursorGlow');
    let mx = -999, my = -999;
    let cx = -999, cy = -999;

    document.addEventListener('mousemove', e => {
        mx = e.clientX;
        my = e.clientY;
    });

    document.addEventListener('mouseleave', () => {
        glow.style.opacity = '0';
    });

    document.addEventListener('mouseenter', () => {
        glow.style.opacity = '1';
    });

    function lerp(a, b, t) { return a + (b - a) * t; }

    function animCursor() {
        cx = lerp(cx, mx, 0.08);
        cy = lerp(cy, my, 0.08);
        glow.style.left = cx + 'px';
        glow.style.top  = cy + 'px';
        requestAnimationFrame(animCursor);
    }
    animCursor();
})();


// ─────────────────────────────────────────────
// 3. NAVBAR SLIDE IN
// ─────────────────────────────────────────────
(function initNavbar() {
    const nav = document.getElementById('navbar');
    setTimeout(() => nav.classList.add('visible'), 200);
})();


// ─────────────────────────────────────────────
// 4. SCROLL REVEAL  (IntersectionObserver)
// ─────────────────────────────────────────────
(function initReveal() {
    const elements = document.querySelectorAll('[data-reveal]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el    = entry.target;
            const delay = parseInt(el.dataset.delay || 0);

            setTimeout(() => {
                el.style.transition = 'opacity 0.65s cubic-bezier(0.22,1,0.36,1), transform 0.65s cubic-bezier(0.22,1,0.36,1)';
                el.style.opacity    = '1';
                el.style.transform  = 'none';

                // hero-line special: animate width
                if (el.classList.contains('hero-line')) {
                    el.style.transition += ', width 0.9s cubic-bezier(0.22,1,0.36,1)';
                    el.style.width = '60%';
                }
            }, delay);

            observer.unobserve(el);
        });
    }, { threshold: 0.15 });

    elements.forEach(el => observer.observe(el));
})();


// ─────────────────────────────────────────────
// 5. FAQ ACCORDION  (smooth height via grid trick)
// ─────────────────────────────────────────────
(function initAccordion() {
    const triggers = document.querySelectorAll('.faq-trigger');

    triggers.forEach(trigger => {
        trigger.addEventListener('click', () => {
            const isOpen = trigger.getAttribute('aria-expanded') === 'true';
            const body   = trigger.nextElementSibling;

            // Close all others
            triggers.forEach(t => {
                if (t !== trigger) {
                    t.setAttribute('aria-expanded', 'false');
                    t.nextElementSibling.classList.remove('open');
                }
            });

            // Toggle current
            trigger.setAttribute('aria-expanded', String(!isOpen));
            body.classList.toggle('open', !isOpen);

            // Ripple spark on open
            if (!isOpen) spawnRipple(trigger);
        });
    });

    function spawnRipple(trigger) {
        const spark = document.createElement('span');
        spark.style.cssText = `
            position:absolute; left:0; top:50%; transform:translateY(-50%);
            width:100%; height:2px;
            background: linear-gradient(90deg, transparent, rgba(0,212,255,0.6), transparent);
            animation: rippleSlide 0.5s ease forwards;
            pointer-events:none;
        `;
        trigger.appendChild(spark);

        // inject keyframe once
        if (!document.getElementById('ripple-kf')) {
            const style = document.createElement('style');
            style.id = 'ripple-kf';
            style.textContent = `
                @keyframes rippleSlide {
                    0%   { clip-path: inset(0 100% 0 0); opacity:1; }
                    70%  { clip-path: inset(0 0% 0 0);   opacity:1; }
                    100% { clip-path: inset(0 0% 0 0);   opacity:0; }
                }
            `;
            document.head.appendChild(style);
        }

        spark.addEventListener('animationend', () => spark.remove());
    }
})();


// ─────────────────────────────────────────────
// 6. GLITCH EFFECT on hero em (random interval)
// ─────────────────────────────────────────────
(function initGlitch() {
    const el = document.querySelector('.glitch');
    if (!el) return;

    function glitch() {
        el.classList.add('glitching');
        setTimeout(() => el.classList.remove('glitching'), 320);
        // Schedule next randomly between 3s and 9s
        setTimeout(glitch, 3000 + Math.random() * 6000);
    }

    // First glitch after page loads
    setTimeout(glitch, 2200);
})();


// ─────────────────────────────────────────────
// 7. FAQ ITEM STAGGERED REVEAL ON LOAD
// ─────────────────────────────────────────────
(function initFaqReveal() {
    const items = document.querySelectorAll('.faq-item[data-reveal]');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el    = entry.target;
            const delay = parseInt(el.dataset.delay || 0) + 300;
            setTimeout(() => {
                el.style.transition = 'opacity 0.55s cubic-bezier(0.22,1,0.36,1), transform 0.55s cubic-bezier(0.22,1,0.36,1)';
                el.style.opacity    = '1';
                el.style.transform  = 'translateY(0)';
            }, delay);
            observer.unobserve(el);
        });
    }, { threshold: 0.1 });

    items.forEach(el => observer.observe(el));
})();


// ─────────────────────────────────────────────
// 8. CONTACT STRIP REVEAL
// ─────────────────────────────────────────────
(function initContactReveal() {
    const strip = document.querySelector('.contact-strip[data-reveal]');
    if (!strip) return;

    const observer = new IntersectionObserver(([entry]) => {
        if (!entry.isIntersecting) return;
        const delay = parseInt(strip.dataset.delay || 0) + 400;
        setTimeout(() => {
            strip.style.transition = 'opacity 0.65s cubic-bezier(0.22,1,0.36,1), transform 0.65s cubic-bezier(0.22,1,0.36,1)';
            strip.style.opacity    = '1';
            strip.style.transform  = 'none';
        }, delay);
        observer.unobserve(strip);
    }, { threshold: 0.2 });

    observer.observe(strip);
})();


// ─────────────────────────────────────────────
// 9. NAVBAR SCROLL SHADOW
// ─────────────────────────────────────────────
(function initNavScroll() {
    const nav = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        nav.style.borderBottomColor = window.scrollY > 20
            ? 'rgba(0,212,255,0.18)'
            : 'rgba(0,212,255,0.10)';
    }, { passive: true });
})();