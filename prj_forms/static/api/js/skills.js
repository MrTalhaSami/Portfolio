// for skills scrolling transition

document.addEventListener("DOMContentLoaded", function () {
  const faders = document.querySelectorAll(".fade-up");

  const appearOptions = {
    threshold: 0.2,
    rootMargin: "0px 0px -50px 0px"
  };

  const appearOnScroll = new IntersectionObserver(function (entries, observer) {
    entries.forEach((entry, index) => {
      if (!entry.isIntersecting) return;

      // Add small delay for staggered effect
      setTimeout(() => {
        entry.target.classList.add("show");
      }, index * 200);

      observer.unobserve(entry.target);
    });
  }, appearOptions);

  faders.forEach(fader => {
    appearOnScroll.observe(fader);
  });
});
