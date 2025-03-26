document.addEventListener("DOMContentLoaded", () => {
    const images = document.querySelectorAll(".clickable-img");

    images.forEach(img => {
        img.addEventListener("click", () => {
            const expanded = document.querySelector(".expanded");

            if (expanded && expanded !== img) {
                expanded.classList.remove("expanded");
                document.body.classList.remove("expanded-mode");
            }

            if (img.classList.contains("expanded")) {
                img.classList.remove("expanded");
                document.body.classList.remove("expanded-mode");
            } else {
                img.classList.add("expanded");
                document.body.classList.add("expanded-mode");
            }
        });
    });
});
