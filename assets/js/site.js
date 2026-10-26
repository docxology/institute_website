const header = document.querySelector(".site-header");

if (header) {
  window.addEventListener(
    "scroll",
    () => {
      header.toggleAttribute("data-scrolled", window.scrollY > 12);
    },
    { passive: true },
  );
}
