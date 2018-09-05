function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function setNumbers() {
  var num = getRandomInt(100);
  document.querySelector('#numberOfPacks').innerHTML = num;
  (num < 10) ? num = '00' + num : num = '0' + num;
  document.querySelector('.counter__digit_left').innerHTML = num[0];
  document.querySelector('.counter__digit_center').innerHTML = num[1];
  document.querySelector('.counter__digit_right').innerHTML = num[2];

}

window.onload = setNumbers;
