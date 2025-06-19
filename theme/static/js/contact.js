 document.getElementById('contactForm').addEventListener('submit', function (event) {
      // 1. Prevent the default form submission
      event.preventDefault();

      // 2. Show a loading alert
      Swal.fire({
        title: 'Sending...',
        text: 'Please wait while we send your message.',
        allowOutsideClick: false,
        didOpen: () => {
          Swal.showLoading();
        },
      });

      const formData = new FormData(this);
      const url = this.action; // The form's action URL

      // 3. Use Fetch API to send the form data
      fetch(url, {
        method: 'POST',
        body: formData,
        headers: {
          'X-Requested-With': 'XMLHttpRequest', // Important for Django to identify AJAX
        },
      })
        .then((response) => response.json()) // Parse the JSON response from the server
        .then((data) => {
          // 4. Handle the server's response
          if (data.success) {
            // If the server response indicates success...
            document.getElementById('contactForm').reset(); // Reset the form fields
            grecaptcha.reset(); // Reset the reCAPTCHA widget

            // Show the success alert you wanted!
            Swal.fire({
              title: 'Success!',
              text: 'Your message has been sent successfully!',
              icon: 'success',
            });
          } else {
            // If the server response indicates an error...
            grecaptcha.reset(); // Reset reCAPTCHA on error too
            const errors = Object.values(data.errors).flat().join('<br>'); // Format errors

            Swal.fire({
              title: 'Oops...',
              html: errors, // Use 'html' to correctly render line breaks
              icon: 'error',
            });
          }
        })
        .catch((error) => {
          // 5. Handle network errors or other unexpected issues
          console.error('Error:', error);
          grecaptcha.reset();

          Swal.fire({
            title: 'An Error Occurred!',
            text: 'Could not send the message. Please check your connection and try again.',
            icon: 'error',
          });
        });
    });