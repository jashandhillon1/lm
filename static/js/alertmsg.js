document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')

if (alertWrapper) {
  alertClose.addEventListener('click', () => {
      alertWrapper.style.display = 'none';
      // console.log("yes");
      }

  )
}