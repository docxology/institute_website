const header = document.querySelector(".site-header");

if (header) {
  let lastY = window.scrollY;
  window.addEventListener(
    "scroll",
    () => {
      const y = window.scrollY;
      header.toggleAttribute("data-scrolled", y > 12);
      lastY = y;
    },
    { passive: true },
  );
}
