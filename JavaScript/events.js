
const firstHead  = document.querySelector('#one')
const secHead = document.querySelector('#two')
const thirdHead = document.querySelector('#third')
const buttonClick = document.querySelector('#btn')
const buttonClick2 = document.querySelector('#btn-2')

firstHead.addEventListener('mouseover', function()
{
    firstHead.textContent = 'Mouse Over';
    firstHead.style.color = 'blue';
}
)


secHead.addEventListener('mouseout', function()
{
    secHead.style.color = 'green'

})


//here v create a function and to get the p ,where v need to appear the text
//while v click the button.
//and select the p and change the text.


function func3() {
  document.querySelector("#para-1").innerHTML = "Hello World";
}

//double click event in dom.

buttonClick.addEventListener('dblclick', function()
{
    buttonClick.textContent = 'Change'
    buttonClick.style.color = 'green'
})

buttonClick2.addEventListener('click', function()
{
    buttonClick.textContent = 'Change'
    buttonClick.style.color = 'green'
})
//
//console.log(firstHead)
//console.log(secHead)
//console.log(thirdHead)



