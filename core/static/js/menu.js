document.addEventListener("DOMContentLoaded", (event) => {
  let button = document.querySelector(".layout__menu-toggle");
  let icon_bars = document.querySelector(".layout__menu-toggle .fa-bars");
  let icon_xmark = document.querySelector(".layout__menu-toggle .fa-xmark");
  let aside = document.querySelector(".header__menu");

  button.addEventListener("click", (event) => {
    let visible = document.querySelector(".header__menu--visible");

    if (!visible) {
      aside.classList.add("header__menu--visible");
      icon_bars.style.opacity = 0;
      icon_xmark.style.opacity = 1;
    } else {
      aside.classList.remove("header__menu--visible");
      icon_bars.style.opacity = 1;
      icon_xmark.style.opacity = 0;
    }
  });
});
