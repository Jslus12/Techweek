document.addEventListener('DOMContentLoaded', () => {
 
    // 1. Cards entram com fade ao carregar a página
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(30px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .card-animado {
            opacity: 0;
            animation: fadeUp 0.5s ease forwards;
        }
    `;
    document.head.appendChild(style);
 
    document.querySelectorAll('.card-dev').forEach((card, i) => {
        card.classList.add('card-animado');
        card.style.animationDelay = (i * 0.1) + 's';
    });
 
    // 2. Navbar some ao rolar para baixo e volta ao rolar para cima
    const navbar = document.getElementById('navbar');
    let ultimoScroll = 0;
 
    window.addEventListener('scroll', () => {
        const scrollAtual = window.scrollY;
 
        navbar.style.transition = 'transform 0.3s ease';
 
        if (scrollAtual > ultimoScroll && scrollAtual > 60) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
 
        ultimoScroll = scrollAtual;
    });
 
});
