// ============ CUSTOM CURSOR ============
const dot = document.querySelector('.cursor-dot');
const ring = document.querySelector('.cursor-ring');
const isCoarse = window.matchMedia('(pointer: coarse)').matches;
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (dot && ring && !isCoarse && !reduceMotion) {
  let mouseX = 0, mouseY = 0;
  let ringX = 0, ringY = 0;

  window.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    dot.style.left = mouseX + 'px';
    dot.style.top = mouseY + 'px';
  });

  function animateRing() {
    ringX += (mouseX - ringX) * 0.18;
    ringY += (mouseY - ringY) * 0.18;
    ring.style.left = ringX + 'px';
    ring.style.top = ringY + 'px';
    requestAnimationFrame(animateRing);
  }
  animateRing();

  document.querySelectorAll('.hoverable, a, button, summary').forEach((el) => {
    el.addEventListener('mouseenter', () => ring.classList.add('active'));
    el.addEventListener('mouseleave', () => ring.classList.remove('active'));
  });
}

// ============ SCROLL REVEAL (zoom / fade in) ============
const revealEls = document.querySelectorAll('[data-reveal], .program-card, .pillar, .testimonial, .faq-item');

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  revealEls.forEach((el) => observer.observe(el));
} else {
  revealEls.forEach((el) => el.classList.add('in-view'));
}

// ============ MOBILE NAV TOGGLE ============
const navToggle = document.getElementById('navToggle');
const navMobile = document.getElementById('navMobile');

if (navToggle && navMobile) {
  navToggle.addEventListener('click', () => {
    navMobile.classList.toggle('open');
  });
  navMobile.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => navMobile.classList.remove('open'));
  });
}
