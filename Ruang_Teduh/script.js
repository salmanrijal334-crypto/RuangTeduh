function makeNav(id, url) {
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('click', () => { window.location.href = url; });
    el.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            window.location.href = url;
        }
    });
}

makeNav('calendar-card', 'calendar.html');
makeNav('activity-card', 'mood-summary.html');