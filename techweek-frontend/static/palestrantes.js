// Navbar
setTimeout(() => document.getElementById('navbar').classList.add('visible'), 100);
 
// Header
document.getElementById('topTag').classList.add('show');
document.getElementById('mainTitle').classList.add('show');
 
// Cards
document.querySelectorAll('.vantage-card').forEach((card, i) => {
    setTimeout(() => card.classList.add('show'), i * 150);
});
