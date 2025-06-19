 const images = [
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg",
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg",
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg",
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg",
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg",
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-6.jpg",
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-7.jpg",
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-8.jpg",
    "https://flowbite.s3.amazonaws.com/docs/gallery/square/image-9.jpg"
  ];

  const gallery = document.getElementById("gallery");
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const prevBtn = document.getElementById("prevBtn");
  const nextBtn = document.getElementById("nextBtn");
  const closeBtn = document.getElementById("closeBtn");

  let currentIndex = 0;

  // Add images to gallery
  images.forEach((src, index) => {
    const img = document.createElement("img");
    img.src = src;
    img.dataset.index = index;
    img.classList.add("w-full", "h-auto", "object-cover","rounded-lg", "shadow-lg", "transition-transform", "duration-500", "hover:scale-105");
    gallery.appendChild(img);
  });

  // Open lightbox on image click
  gallery.addEventListener("click", (e) => {
    if (e.target.tagName === "IMG") {
      currentIndex = parseInt(e.target.dataset.index);
      lightboxImg.src = images[currentIndex];
      lightbox.classList.remove("hidden");
    }
  });

  // Navigate to previous image
  prevBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    lightboxImg.src = images[currentIndex];
  });

  // Navigate to next image
  nextBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    currentIndex = (currentIndex + 1) % images.length;
    lightboxImg.src = images[currentIndex];
  });

  // Close lightbox using close button
  closeBtn.addEventListener("click", (e) => {
    e.stopPropagation(); // Prevent event from bubbling to lightbox
    lightbox.classList.add("hidden");
  });

  // Optional: clicking outside image (on overlay) also closes
  lightbox.addEventListener("click", (e) => {
    if (e.target === lightbox) {
      lightbox.classList.add("hidden");
    }
  });